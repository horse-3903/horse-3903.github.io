/* Update frontmatter published date based on file mtime */

import fs from "fs";
import path from "path";

const POSTS_DIR = path.join("src", "content", "posts");
const FILE_EXTENSIONS = new Set([".md", ".mdx"]);

function formatDate(date) {
	const year = date.getFullYear();
	const month = String(date.getMonth() + 1).padStart(2, "0");
	const day = String(date.getDate()).padStart(2, "0");
	return `${year}-${month}-${day}`;
}

function getEol(content) {
	return content.includes("\r\n") ? "\r\n" : "\n";
}

function hasFrontmatter(content) {
	return content.startsWith("---");
}

function updateFrontmatter(content, publishedDate) {
	const eol = getEol(content);
	const match = content.match(/^---\s*\r?\n([\s\S]*?)\r?\n---\s*\r?\n?/);
	if (!match) {
		return { updated: false, content };
	}

	const fm = match[1];
	const lines = fm.split(/\r?\n/);
	let found = false;

	for (let i = 0; i < lines.length; i += 1) {
		if (lines[i].startsWith("published:")) {
			lines[i] = `published: ${publishedDate}`;
			found = true;
			break;
		}
	}

	if (!found) {
		const titleIndex = lines.findIndex((line) => line.startsWith("title:"));
		const insertAt = titleIndex >= 0 ? titleIndex + 1 : 0;
		lines.splice(insertAt, 0, `published: ${publishedDate}`);
	}

	const newFrontmatter = `---${eol}${lines.join(eol)}${eol}---${eol}`;
	const rest = content.slice(match[0].length);

	return { updated: true, content: newFrontmatter + rest, eol };
}

function walk(dir) {
	const entries = fs.readdirSync(dir, { withFileTypes: true });
	const files = [];

	for (const entry of entries) {
		const fullPath = path.join(dir, entry.name);
		if (entry.isDirectory()) {
			files.push(...walk(fullPath));
			continue;
		}

		if (FILE_EXTENSIONS.has(path.extname(entry.name).toLowerCase())) {
			files.push(fullPath);
		}
	}

	return files;
}

function normalizePath(inputPath) {
	return path.isAbsolute(inputPath)
		? inputPath
		: path.join(process.cwd(), inputPath);
}

function updateFile(filePath) {
	const stat = fs.statSync(filePath);
	const publishedDate = formatDate(stat.mtime);
	const content = fs.readFileSync(filePath, "utf8");

	if (!hasFrontmatter(content)) {
		return { filePath, status: "skipped (no frontmatter)" };
	}

	const result = updateFrontmatter(content, publishedDate);
	if (!result.updated) {
		return { filePath, status: "skipped (invalid frontmatter)" };
	}

	if (result.content === content) {
		return { filePath, status: "unchanged" };
	}

	fs.writeFileSync(filePath, result.content, "utf8");
	return { filePath, status: `updated (${publishedDate})` };
}

const args = process.argv.slice(2);
const targetFiles =
	args.length > 0
		? args.map((arg) => normalizePath(arg))
		: walk(POSTS_DIR).map((file) => normalizePath(file));

if (targetFiles.length === 0) {
	console.error("No files found to update.");
	process.exit(1);
}

const results = targetFiles.map(updateFile);
const updatedCount = results.filter((r) => r.status.startsWith("updated")).length;
const skippedCount = results.filter((r) => r.status.startsWith("skipped")).length;

for (const result of results) {
	console.log(`${result.status}: ${result.filePath}`);
}

console.log(
	`Done. Updated ${updatedCount} file(s), skipped ${skippedCount} file(s).`,
);

/* Ensure markdown files have required frontmatter header when missing. */

import { promises as fs } from "fs";
import path from "path";

const POSTS_DIR = path.join(process.cwd(), "src", "content", "posts");

function formatDate(date) {
	const year = date.getFullYear();
	const month = String(date.getMonth() + 1).padStart(2, "0");
	const day = String(date.getDate()).padStart(2, "0");
	return `${year}-${month}-${day}`;
}

async function listMarkdownFiles(dir) {
	const entries = await fs.readdir(dir, { withFileTypes: true });
	const files = [];
	for (const entry of entries) {
		const fullPath = path.join(dir, entry.name);
		if (entry.isDirectory()) {
			files.push(...(await listMarkdownFiles(fullPath)));
		} else if (entry.isFile() && entry.name.toLowerCase().endsWith(".md")) {
			files.push(fullPath);
		}
	}
	return files;
}

function buildHeader(filePath) {
	const baseName = path.basename(filePath, path.extname(filePath));
	const today = formatDate(new Date());
	return (
		"---\n" +
		`title: ${baseName}\n` +
		`published: ${today}\n` +
		"description: \"\"\n" +
		"tags: []\n" +
		"category: \"\"\n" +
		"draft: false\n" +
		"---\n\n"
	);
}

async function ensureFrontmatter() {
	const files = await listMarkdownFiles(POSTS_DIR);
	let updatedCount = 0;

	for (const filePath of files) {
		const content = await fs.readFile(filePath, "utf8");
		if (content.startsWith("---")) {
			continue;
		}
		const header = buildHeader(filePath);
		await fs.writeFile(filePath, header + content, "utf8");
		updatedCount += 1;
	}

	console.log(`ensure-frontmatter: added headers to ${updatedCount} file(s).`);
}

ensureFrontmatter().catch((error) => {
	console.error("ensure-frontmatter failed:", error);
	process.exit(1);
});

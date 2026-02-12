/* Convert common American spellings to British in markdown content. */

import fs from "fs";
import path from "path";

const POSTS_DIR = path.join("src", "content", "posts");
const FILE_EXTENSIONS = new Set([".md", ".mdx"]);

const WORD_MAP = new Map([
	["color", "colour"],
	["colors", "colours"],
	["favorite", "favourite"],
	["favorites", "favourites"],
	["organize", "organise"],
	["organizes", "organises"],
	["organized", "organised"],
	["organizing", "organising"],
	["optimize", "optimise"],
	["optimizes", "optimises"],
	["optimized", "optimised"],
	["optimizing", "optimising"],
	["initialize", "initialise"],
	["initializes", "initialises"],
	["initialized", "initialised"],
	["initializing", "initialising"],
	["normalize", "normalise"],
	["normalizes", "normalises"],
	["normalized", "normalised"],
	["normalizing", "normalising"],
	["standardize", "standardise"],
	["standardizes", "standardises"],
	["standardized", "standardised"],
	["standardizing", "standardising"],
	["minimize", "minimise"],
	["minimizes", "minimises"],
	["minimized", "minimised"],
	["minimizing", "minimising"],
	["maximize", "maximise"],
	["maximizes", "maximises"],
	["maximized", "maximised"],
	["maximizing", "maximising"],
	["analyze", "analyse"],
	["analyzes", "analyses"],
	["analyzed", "analysed"],
	["analyzing", "analysing"],
	["modeling", "modelling"],
	["modeled", "modelled"],
	["modeler", "modeller"],
	["traveler", "traveller"],
	["travelers", "travellers"],
	["center", "centre"],
	["centers", "centres"],
	["meter", "metre"],
	["meters", "metres"],
	["liter", "litre"],
	["liters", "litres"],
	["neighbor", "neighbour"],
	["neighbors", "neighbours"],
	["behavior", "behaviour"],
	["behaviors", "behaviours"],
	["favor", "favour"],
	["favors", "favours"],
	["honor", "honour"],
	["honors", "honours"],
	["rumor", "rumour"],
	["rumors", "rumours"],
	["theater", "theatre"],
	["theaters", "theatres"],
	["gray", "grey"],
	["license", "licence"],
	["licenses", "licences"],
	["defense", "defence"],
	["offense", "offence"],
	["catalog", "catalogue"],
	["catalogs", "catalogues"],
	["program", "programme"],
	["programs", "programmes"],
]);

const RULES = [
	{
		name: "or->our",
		pattern: /(\w+?)or\b/gi,
		replace: (word) => {
			if (word.length < 5) return null;
			if (/(tour|pour|sour|your|four|minor|major|actor|editor|author)$/i.test(word)) {
				return null;
			}
			return word.replace(/or$/i, "our");
		},
	},
	{
		name: "ize->ise",
		pattern: /\b\w+ize(s|d|r|rs|ing)?\b/gi,
		replace: (word) => word.replace(/ize/gi, "ise"),
	},
	{
		name: "ization->isation",
		pattern: /\b\w+ization(s)?\b/gi,
		replace: (word) => word.replace(/ization/gi, "isation"),
	},
	{
		name: "yze->yse",
		pattern: /\b\w+yze(s|d|r|rs|ing)?\b/gi,
		replace: (word) => word.replace(/yze/gi, "yse"),
	},
	{
		name: "er->re (centre, metre)",
		pattern: /\b(?:center|centers|meter|meters|liter|liters|theater|theaters)\b/gi,
		replace: (word) => {
			const lower = word.toLowerCase();
			const lookup = {
				center: "centre",
				centers: "centres",
				meter: "metre",
				meters: "metres",
				liter: "litre",
				liters: "litres",
				theater: "theatre",
				theaters: "theatres",
			};
			return applyCase(word, lookup[lower] ?? word);
		},
	},
	{
		name: "og->ogue",
		pattern: /\b\w+og(s)?\b/gi,
		replace: (word) => {
			if (/(blog|log|dog|fog|prog|hog|cog|og)$/i.test(word)) {
				return null;
			}
			return word.replace(/og(s)?$/i, "ogue$1");
		},
	},
	{
		name: "lling (traveling, modeling)",
		pattern: /\b\w+l(ing|ed|er|ers)\b/gi,
		replace: (word) => {
			if (/(modeling|modeled|modeler|modelers|traveling|traveled|traveler|travelers)$/i.test(word)) {
				return applyCase(word, WORD_MAP.get(word.toLowerCase()) ?? word);
			}
			return null;
		},
	},
];

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

function isUrlToken(token) {
	return token.includes("://") || token.startsWith("www.");
}

function applyCase(source, replacement) {
	if (source.toUpperCase() === source) {
		return replacement.toUpperCase();
	}
	if (source[0]?.toUpperCase() === source[0]) {
		return replacement[0].toUpperCase() + replacement.slice(1);
	}
	return replacement;
}

function replaceInText(text) {
	let updated = text;

	for (const rule of RULES) {
		updated = updated.replace(rule.pattern, (match) => {
			if (isUrlToken(match)) return match;
			const replaced = rule.replace(match);
			return replaced ?? match;
		});
	}

	const words = Array.from(WORD_MAP.keys()).join("|");
	if (words.length > 0) {
		const regex = new RegExp(`\\b(${words})\\b`, "gi");
		updated = updated.replace(regex, (match) => {
			if (isUrlToken(match)) {
				return match;
			}
			const lower = match.toLowerCase();
			const replacement = WORD_MAP.get(lower);
			if (!replacement) {
				return match;
			}
			return applyCase(match, replacement);
		});
	}

	return updated;
}

function replaceInLinePreservingCode(line) {
	// Split on inline code blocks to avoid changing code.
	const parts = line.split(/(`[^`]*`)/g);
	return parts
		.map((part) => {
			if (part.startsWith("`") && part.endsWith("`")) {
				return part;
			}
			return replaceInText(part);
		})
		.join("");
}

function processContent(content) {
	const lines = content.split(/\r?\n/);
	let inFence = false;
	let fenceDelimiter = "";

	const out = lines.map((line) => {
		const fenceMatch = line.match(/^(\s*)(`{3,}|~{3,})/);
		if (fenceMatch) {
			const delimiter = fenceMatch[2];
			if (!inFence) {
				inFence = true;
				fenceDelimiter = delimiter;
			} else if (delimiter === fenceDelimiter) {
				inFence = false;
				fenceDelimiter = "";
			}
			return line;
		}

		if (inFence) {
			return line;
		}

		return replaceInLinePreservingCode(line);
	});

	return out.join(content.includes("\r\n") ? "\r\n" : "\n");
}

function normalizePath(inputPath) {
	return path.isAbsolute(inputPath)
		? inputPath
		: path.join(process.cwd(), inputPath);
}

function updateFile(filePath) {
	const content = fs.readFileSync(filePath, "utf8");
	const updated = processContent(content);

	if (updated === content) {
		return { filePath, status: "unchanged" };
	}

	fs.writeFileSync(filePath, updated, "utf8");
	return { filePath, status: "updated" };
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
const updatedCount = results.filter((r) => r.status === "updated").length;

for (const result of results) {
	console.log(`${result.status}: ${result.filePath}`);
}

console.log(`Done. Updated ${updatedCount} file(s).`);

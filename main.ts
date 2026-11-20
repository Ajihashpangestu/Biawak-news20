import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const input = new URL("./entry.png", import.meta.url);
if (!existsSync(input)) {
  execFileSync("sh", [fileURLToPath(new URL("./render.sh", import.meta.url))], { stdio: "inherit" });
}
const image = readFileSync(input);
const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const written = join(outDir, "entry.png");

mkdirSync(outDir, { recursive: true });
writeFileSync(written, image);
console.log(JSON.stringify({
  written,
  bytes: image.length,
  sha256: createHash("sha256").update(image).digest("hex"),
}));

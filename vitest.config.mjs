import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    environment: "jsdom",
    globals: true,
    pool: "threads",
    include: ["tests/unit/**/*.test.{js,mjs}"],
    setupFiles: ["tests/unit/setup.js"],
    coverage: {
      provider: "v8",
      reporter: ["text", "json-summary"],
      include: ["scripts.js"],
    },
  },
});

module.exports = {
  branches: ["main"],
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    {
      '@semantic-release/github': {
        assets: [
          { path: '/*.js', label: 'JavaScript files'}, // Ajusta según tus necesidades
        ],
      },
    },
  ],
};

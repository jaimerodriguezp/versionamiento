module.exports = {
  branches: ["main"],
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    {
      '@semantic-release/github': {
        assets: [
          { path: 'dist/*.js', label: 'JavaScript distribution' }, // Ajusta según tus necesidades
        ],
      },
    },
  ],
};

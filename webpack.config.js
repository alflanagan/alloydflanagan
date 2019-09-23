var path = require('path')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  mode: 'development',
  context: __dirname,
  entry: './assets/js/index',
  output: {
    path: path.resolve('./assets/webpack_bundles/'),
    filename: '[name]-[hash].js'
  },

  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: './webpack-stats.json'
    })
  ],
  module: {
    rules: [
      { test: /\.jsx?$/, exclude: /node_modules/, use: 'babel-loader' }
    ]
  },

  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.jsx']
  }
}

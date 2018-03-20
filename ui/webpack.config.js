const webpack = require('webpack');
const path = require('path');

// dist and contentBase for dev-server have to be same. Eww
const DISTDIR = path.resolve(__dirname, 'dist')

module.exports = {
  entry: [
    'react-hot-loader/patch',
    './src/index.js'
  ],

  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },

  resolve: {
    modules: [
      path.join(__dirname, 'src'),
      'node_modules',
    ],
    extensions: ['*', '.js', '.jsx']
  },

  output: {
    filename: 'bundle.js',
    path: DISTDIR
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin()
  ],

  devServer: {
    contentBase: DISTDIR,
    hot: true
  }

};


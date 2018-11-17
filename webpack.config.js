module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        use: {
            loader: "babel-loader"
        }
      },
      { // sass / scss loader for webpack
        test: /\.(sass|scss)$/,
        use: [
            'style-loader',
            'css-loader',
            'resolve-url-loader',
            'sass-loader?sourceMap'
        ],
      },
      {
        test: /\.(jpg|png|gif)$/,
        use: {
            loader: "file-loader",
            options: {
                name: "[path][name].[hash].[ext]",
            },
        },
      },
      {
        test: /\.svg$/,
        use: "file-loader",
      },
    ]
  }
};
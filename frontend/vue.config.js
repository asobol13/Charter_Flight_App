// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })

module.exports = {
  pages: {
    index: {
      // entry for the page
      entry: 'src/pages/Home/main.js',
      // the source template
      template: 'public/index.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Home Page',
      // chunks to include on this page, by default includes
      // extracted common chunks and vendor chunks.
      chunks: ['chunk-vendors', 'chunk-common', 'index']
    },
    'Customers': {
      entry: 'src/pages/Customers/main.js',
      template: 'public/index.html',
      title: 'CustomersPage',
      chunks: ['chunk-vendors', 'chunk-common', 'Customers']
    },
    'Charters': {
      entry: 'src/pages/Charters/main.js',
      template: 'public/index.html',
      title: 'ChartersPage',
      chunks: ['chunk-vendors', 'chunk-common', 'Charters']
    },
    'Pilots': {
      entry: 'src/pages/Pilots/main.js',
      template: 'public/index.html',
      title: 'PilotsPage',
      chunks: ['chunk-vendors', 'chunk-common', 'Pilots']
    },
    'Aircrafts': {
      entry: 'src/pages/Aircrafts/main.js',
      template: 'public/index.html',
      title: 'AircraftsPage',
      chunks: ['chunk-vendors', 'chunk-common', 'Aircrafts']
    }
  }
}

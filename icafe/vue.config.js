module.exports = {
    runtimeCompiler: true,
    baseUrl: (function () {
        return {
            development: undefined,
            production: './',
            preview: './'
        }[process.env.NODE_ENV] || undefined;
    })(),
}
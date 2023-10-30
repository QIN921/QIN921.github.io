window.MathJax = {
    tex: {
        inlineMath: [["\\(", "\\)"], ['$', '$']],
        displayMath: [["\\[", "\\]"]],
        processEscapes: true,
        processEnvironments: true,
        autoload: { color: [], colorV2: ["color"] },
        packages: { "[+]": ["noerrors"] }
    },
    options: {
        // ignoreHtmlClass: ".*|",
        // processHtmlClass: "arithmatex"
        ignoreHtmlClass: "tex2jax_ignore",
        processHtmlClass: "tex2jax_process"
    },
    loader: { load: ["input/asciimath", "[tex]/noerrors", "[tex]/mhchem"] }
};

document$.subscribe(() => {
    MathJax.typesetPromise()
})

$('link').each(function () {
    var $intial = $(this).attr('href'),
        $replace = $intial.replace('fonts.googleapis.com/', 'fonts.font.im/');
    console.log($intial);
    console.log($replace);
    $(this).attr('href', $replace);
});


WebFont.load({
    custom: {
        families: ['Noto Sans SC', 'Ubuntu Mono', 'Roboto']
    }
});

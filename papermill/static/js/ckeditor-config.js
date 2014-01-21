CKEDITOR.editorConfig = function( config ) {
    // %REMOVE_START%
    config.skin = 'moono';
    // %REMOVE_END%

    // The toolbar groups arrangement, optimized for a single toolbar row.
    config.toolbarGroups = [
        { name: 'document',    groups: [ 'mode', 'document', 'doctools' ] },
        { name: 'clipboard',   groups: [ 'clipboard', 'undo' ] },
        { name: 'editing',     groups: [ 'find', 'selection', 'spellchecker' ] },
        { name: 'forms' },
        { name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ] },
        { name: 'paragraph',   groups: [ 'list', 'indent', 'blocks', 'align', 'bidi' ] },
        { name: 'links' },
        { name: 'insert' },
        { name: 'styles' },
        { name: 'colors' },
        { name: 'tools' },
        { name: 'about' }
    ];

    config.removeButtons = 'Cut,Copy,Paste,Undo,Redo,Anchor,Underline,Strike,Subscript,Superscript';

    config.removeDialogTabs = 'link:advanced';

    config.plugins = 'link,wysiwygarea,toolbar,sourcearea,image,imagebrowser,filebrowser,blockquote,basicstyles,stylescombo,pastetext,removeformat,list,oembed';
    config.extraAllowedContent = 'h1 h2 h3 h4 h5 h6';
    config.stylesSet =[
        { name: 'Overskrift 1', element: 'h1' },
        { name: 'Overskrift 2', element: 'h2' },
        { name: 'Overskrift 3', element: 'h3' },
        { name: 'Overskrift 4', element: 'h4' },
        { name: 'Overskrift 5', element: 'h5' },
        { name: 'Overskrift 6', element: 'h6' },
    ];
    config.height = '400px';
    config.filebrowserBrowseUrl = '/admin/papermill/imgs/browser/';
};

CKEDITOR.on('instanceReady', function(ev) {
    ev.editor.dataProcessor.htmlFilter.addRules( {
        elements: {
            img: function( el ) {
                el.className = 'img-responsive';
                el.attributes.class = 'img-responsive';
                el.attributes.style = '';
            }
        }
    });
});

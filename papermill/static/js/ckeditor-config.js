CKEDITOR.editorConfig = function( config ) {
    // %REMOVE_START%
    config.skin = 'moono';
    // %REMOVE_END%
    config.language = 'nb';

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
                el.attributes.height = '';
                el.attributes.width = '';
            }
        }
    });
});

CKEDITOR.on('dialogDefinition', function (ev) {
    // Take the dialog name and its definition from the event data.
    var dialogName = ev.data.name;
    var dialogDefinition = ev.data.definition;
    // Check if the definition is from the dialog we're
    // interested in (the 'image' dialog).
    if (dialogName == 'image') {
        // Get a reference to the 'Image Info' tab.
        var infoTab = dialogDefinition.getContents('info');
        // Remove unnecessary widgets/elements from the 'Image Info' tab.

        infoTab.remove('txtHSpace');
        infoTab.remove('txtVSpace');
        infoTab.remove('txtBorder');

        infoTab.remove('cmbAlign');
        infoTab.remove('ratioLock');

    }
});


    $(function(){
        if ($.infinitescroll) {
            var $container = $('#posts');

            $container.infinitescroll({
                // selector for the paged navigation
                navSelector  : '#page_nav',
                // selector for the NEXT link (to page 2)
                nextSelector : '#page_nav a',
                // selector for all items you'll retrieve
                itemSelector : '.post-wrapper',
                loading: {
                    msgText: 'Loading next set of posts..',
                    finishedMsg: 'No more posts to load.',
                    img: 'http://i.imgur.com/qkKy8.gif',
                    speed: 0
                  }
                },
                // call Isotope as a callback
                function( newElements ) {

                }
            );
        }
    });
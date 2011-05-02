/**
 * @file domcleanup plugin
 * 
 * Simplifies and sanitizes inserted (including pasted) HTML.
 */

CKEDITOR.plugins.add( 'domcleanup',
{
    init : function( editor )
    {
        var allowed_tags = ['p','a','em','strong','u','img','h1','h2','h3',
        'h4','h5','hr','ul','ol','li','table','thead','tbody','tr','th','td',
        'strike','sub','sup'];
        if(editor.config.domcleanupAllowedTags)
            allowed_tags = editor.config.domcleanupAllowedTags;
        editor.plugins['domcleanup'].allowedTags = allowed_tags;

        editor.on( 'paste', function( evt )
        {
        // haven't had to customize this, yet
        });
        
    },
    afterInit : function( editor )
    {
        // fix Array.indexOf in IE (we use it later)
        if(!Array.indexOf){
            Array.prototype.indexOf = function(obj){
                for(var i=0; i<this.length; i++){
                    if(this[i]==obj){
                        return i;
                    }
                }
                return -1;
            }
        }
        var dataProcessor = editor.dataProcessor,
        dataFilter = dataProcessor && dataProcessor.dataFilter;
        if ( dataFilter )
        {
            dataFilter.addRules(
            {
                elements :
                {
                    $ : function (element)
                    {
                        element.name = element.name.toLowerCase();
                        var drop_tags = ['style','script','head'];
                        if(drop_tags.indexOf(element.name) != -1)
                            return false;
                        var ok_tags = editor.plugins['domcleanup'].allowedTags;
                        var ok_attributes = {
                            'p' : ['style'],
                            'a' : ['name','href'],
                            'img' : ['src','alt','title','style','class'],
                            'span' : ['class','style'],
                            'table' : ['class','style'],
                            'th': ['colspan','rowspan','style'],
                            'td': ['colspan','rowspan','style']
                        };
                        for(attr in element.attributes)
                        {
                        	if(attr.indexOf('data-cke-') == 0)
                        		continue;
                            if(!ok_attributes[element.name] ||
                                ok_attributes[element.name]
                                                .indexOf(attr) < 0){
                                delete element.attributes[attr];
                            }
                     
                        }
                        if(ok_tags.indexOf(element.name) > -1)
                            return element;
                        var remap = {'br':'p',
                                     'i': 'em',
                                     'b': 'strong'
                                    };
                        if(remap[element.name])
                        {
                            element.name = remap[element.name];
                            if(element.isEmpty &&
                              !(element.children && element.children.length) &&
                              element.parent && element.parent.name == 'p' &&
                              element.parent.children.length == 1)
                                element.name = '';
                        }
                        else element.name = '';
                        return element;
                    }
                }
            });
        }
    }
} );


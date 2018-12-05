#PYOMS - python frontend

##pip install git+https://github.com/DJWOMS/pyoms

python on js

cd example\render                                                                                
build file                                                                                       
python -m http.server                                                                            
http://localhost:8000/example/

HTML
`<script type="module">
   import * as app from './static/__target__/start.js';
   window.app = app;
 </script>`
 
##Binding values

Transparency binds values in-place. That means, you don't need to write separate template sections on your page. Instead, compose just a normal, static html page and start binding some dynamic values on it!

By default, Transparency binds dict to a DOM element by id, class,name attribute and data-bind 
attribute. Default behavior can be changed by providing a custom matcher function, as explained in section Configuration. Values are escaped before rendering.


    <div id="template">
      <span class="greeting"></span>
      <span data-bind="name"></span>
    </div>
    
    hello = {
      'greeting': 'Hello',
      'name':     'world!'
    };
    
    Inner('#template').render(hello);
    
    Result:
    <div id="template">
      <span class="greeting">Hello</span>
      <span data-bind="name">world!</span>
    </div>

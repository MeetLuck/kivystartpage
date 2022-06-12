1. flow~

                                                                          
                Widget1(Cal)    Widget1(Cal)         +---------Wiget2(Off)                  
                      ^            ^                 |            |          
                      |            |                 |            |           
                   <child>      <child>           <parent>     *app.root*    
                      |            |                 |            |          
                      |            |                 |            |          
                      +--------- |Root|(MyStartBox) <--+------------|
                                   ^                                      
                                   |                                      
                                   |                                      
                                  *app*                                    
                                                                          
#2. kivy.config#
  https://kivy.org/doc/stable/api-kivy.config.html

  custom titlebar~
    graphics - custom_titlebar --> https://kivy.org/doc/stable/api-kivy.core.window.html#kivy.core.window.WindowBase.set_custom_titlebar

#3.kivy.core.window#
  no title bar~
    Window.borderless = True





 vim: set et ts=2 sw=2 sts=2 ft=help textwidth=0:

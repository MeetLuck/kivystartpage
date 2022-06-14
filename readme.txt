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
                                                                          
2. kivy.config~
  https://kivy.org/doc/stable/api-kivy.config.html

  custom titlebar~
    graphics - custom_titlebar --> https://kivy.org/doc/stable/api-kivy.core.window.html#kivy.core.window.WindowBase.set_custom_titlebar

3.kivy.core.window~
  no title bar~
    Window.borderless = True

4. floatlayout~
  must set 'resizable' True
  `Config.set('graphics','resizable',True)`

5. clock~
  # call my_callback as soon as possible (usually next frame.)
  `Clock.schedule_once(my_callback)`
  Note
  If the callback returns False, the schedule will be canceled and won’t repeat.
  If you want to schedule a function to call with default arguments, you can use the functools.partial python module:

  `from functools import partial`
  def my_callback(value, key, *args):
      pass
  Clock.schedule_interval( partial(my_callback, 'value', 'key'), 0.5)






 vim: set et ts=2 sw=2 sts=2 ft=help textwidth=0:

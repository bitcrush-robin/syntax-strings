def test():
    sql = '''--begin-sql
    SELECT * FROM a
    ;'''

    html = '''<html>
    <span class="fsdafsd">sdfds</span>
    </html>'''

    py = '''#python
        def fart():
            pass
        #endpython'''

    glsl = '''#version 120

    attribute vec3 position;
    uniform float test;
    void main(){
        gl_Position = vec4(position.xy, test, 0.);
    }
    //end-glsl
    '''

    range(2)

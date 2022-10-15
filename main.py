import moderngl_window as mglw

class App(mglw.WindowConfig):
    window_size = 1600, 900
    resource_dir = 'programs'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.quad = mglw.geometry.quad_fs()
        self.program = self.load_program(vertex_shader='vertex.glsl', fragment_shader='fragment.glsl')
        # Uniforms
        self.program['u_resolution'] = self.window_size


    def render(self, time, frame_time):
        self.ctx.clear()
        self.quad.render(self.program)


if __name__ == '__main__':
    mglw.run_window_config(App)






























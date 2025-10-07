class Graphics:
    def __init__(self, ctx, model, material):
        self.__ctx = ctx
        self.__model = model
        self.__material = material

        self.__vbo = self.create_buffers()
        self.__ibo = ctx.buffer(model.indices.tobytes())
        self.__vao = ctx.vertex_array(material.shader_program.prog, [*self.__vbo], self.__ibo)
        self.__textures = self.load_textures(material.textures_data)

    def create_buffers(self):
        buffers = []
        shader_attributes = self.__material.shader_program.attributes

        for attribute in self.__model.vertex_layout.get_attributes():
            if attribute.name in shader_attributes:
                vbo = self.__ctx.buffer(attribute.array.tobytes())
                buffers.append((vbo, attribute.format, attribute.name))
        return buffers

    def load_textures(self, textures_data):
        textures = []
        for texture in textures_data:
            if texture.image_data:
                texture_ctx = self.__ctx.texture(texture.size, texture.channels_amount, texture.get_bytes())
                if texture.build_mipmaps:
                    texture_ctx.build_mipmaps()
                texture_ctx.repeat_x = texture.repeat_x
                texture_ctx.repeat_y = texture.repeat_y
                textures.append((texture.name, texture_ctx))
        return textures

    def bind_to_image(self, name = "u_texture", unit = 0, read = False, write = True):
        self.__textures[name][1].bind_to_image(unit, read, write)

    def update_texture(self, name, texture_data):
        # Encontrar la textura por nombre y actualizar sus datos
        for i, (tex_name, texture_ctx) in enumerate(self.__textures):
            if tex_name == name:
                texture_ctx.write(texture_data.tobytes())
                break

    def render(self, uniforms):
        for name, value in uniforms.items():
            if name in self.__material.shader_program.prog:
                self.__material.set_uniform(name, value)

        for i, (name, texture_ctx) in enumerate(self.__textures):
            texture_ctx.use(i)
            self.__material.shader_program.set_uniform(name, i)

        self.__vao.render()


class ComputeGraphics(Graphics):
    def __init__(self, ctx, model, material):
        self.__ctx = ctx
        self.__model = model
        self.__material = material
        self.textures = material.textures_data
        super().__init__(ctx, model, material)

    def create_primitive(self, primitives):
        amin, amax = self.__model.aabb
        primitives.append({'aabb_min': amin, 'aabb_max': amax})

    def create_transformation_matrix(self, transformations_matrix, index):
        m = self.__model.get_model_matrix()
        transformations_matrix[index, :] = np.array(m.to_list(), dtype='f4').reshape(16)

    def create_inverse_transformation_matrix(self, inverse_transformations_matrix, index):
        m = self.__model.get_model_matrix()
        inverse = glm.inverse(m)
        inverse_transformations_matrix[index, :] = np.array(inverse.to_list(), dtype='f4').reshape(16)

    def create_material_matrix(self, materials_matrix, index):
        reflectivity = self.__material.reflectivity
        r,g,b = self.__material.colorRGB

        r = r /255.0 if r > 1.0 else r
        g = g /255.0 if g > 1.0 else g
        b = b /255.0 if b > 1.0 else b

        materials_matrix[index, :] = np.array([r, g, b, reflectivity], dtype='f4')
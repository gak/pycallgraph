import xmlrpclib

class Ubigraph:
  def __init__(self, URL='http://127.0.0.1:20738/RPC2'):
    self.server = xmlrpclib.Server(URL)
    self.server_backup = self.server
    self.defaultVertexStyle = VertexStyle(self, None, id=0)
    self.defaultEdgeStyle = EdgeStyle(self, None, id=0)

  def clear(self):
    self.server.ubigraph.clear()
    
  def beginMultiCall(self):
    self.server = xmlrpclib.MultiCall(self.server)
    
  def endMultiCall(self):
    for result in self.server():
      print result
    self.server = self.server_backup

  def newVertex(self, id=None, style=None, color=None, shape=None,
                label=None, size=None, fontcolor=None, fontfamily=None,
                fontsize=None, visible=None):
    return Vertex(self, id=id, style=style, color=color, shape=shape,
      label=label, size=size, fontcolor=fontcolor, fontfamily=fontfamily,
      fontsize=fontsize, visible=visible)
                
  def newEdge(self, x, y, id=None, style=None, arrow=None, arrow_position=None,
             arrow_length=None, arrow_radius=None, arrow_reverse=None,
             color=None, label=None, fontcolor=None, fontfamily=None, 
             fontsize=None, oriented=None, spline=None, showstrain=None, 
             stroke=None, strength=None, visible=None, width=None):
    return Edge(self, x, y, id=id, style=style, arrow=arrow, 
      arrow_position=arrow_position, arrow_length=arrow_length,
      arrow_radius=arrow_radius, arrow_reverse=arrow_reverse, color=color,
      label=label, fontcolor=fontcolor, fontfamily=fontfamily, 
      fontsize=fontsize, oriented=oriented, spline=spline, 
      showstrain=showstrain, stroke=stroke, strength=strength,
      visible=visible, width=width)
    
  def newVertexStyle(self, parentStyle=None, id=None, color=None, shape=None,
                label=None, size=None, fontcolor=None, fontfamily=None,
                fontsize=None, visible=None):
    return VertexStyle(self, parentStyle=parentStyle, id=id,
      color=color, shape=shape, label=label, size=size, fontcolor=fontcolor,
      fontfamily=fontfamily, fontsize=fontsize, visible=visible)

  def newEdgeStyle(self, parentStyle=None, id=None, arrow=None, 
             arrow_position=None, arrow_length=None, arrow_radius=None, 
             arrow_reverse=None, color=None,
             label=None, fontcolor=None, fontfamily=None, fontsize=None,
             oriented=None, spline=None, showstrain=None, stroke=None,
             strength=None, visible=None, width=None):
    return EdgeStyle(self, parentStyle=parentStyle, id=id, arrow=arrow,
      arrow_position=arrow_position, arrow_length=arrow_length, 
      arrow_radius=arrow_radius, color=color, label=label, 
      fontcolor=fontcolor, fontfamily=fontfamily,
      fontsize=fontsize, oriented=oriented, spline=spline,
      showstrain=showstrain, stroke=stroke, strength=strength,
      visible=visible, width=width)



class Vertex:
  def __init__(self, U, id=None, style=None, color=None, shape=None,
      label=None, size=None, fontcolor=None, fontfamily=None, fontsize=None, 
      visible=None, callback=None):
    self.U = U
    if id == None:
      self.id = U.server.ubigraph.new_vertex()
    else:
      U.server.ubigraph.new_vertex_w_id(id)
      self.id = id
    self.set(style=style, color=color, shape=shape, label=label, 
      size=size, fontcolor=fontcolor, fontfamily=fontfamily, 
      fontsize=fontsize, visible=visible, callback=callback)

  def set(self, style=None, color=None, shape=None,
      label=None, size=None, fontcolor=None, fontfamily=None, fontsize=None,
      visible=None, callback=None):
    if style != None:
      self.U.server.ubigraph.change_vertex_style(self.id, style.id)
    if color != None:
      self.U.server.ubigraph.set_vertex_attribute(self.id, "color", color)
    if shape != None:
      self.U.server.ubigraph.set_vertex_attribute(self.id, "shape", shape)
    if label != None:
      self.U.server.ubigraph.set_vertex_attribute(self.id, "label", label)
    if size != None:
      self.U.server.ubigraph.set_vertex_attribute(self.id, "size", str(size))
    if fontcolor != None:
      self.U.server.ubigraph.set_vertex_attribute(self.id, "fontcolor", fontcolor)
    if fontfamily != None:
      self.U.server.ubigraph.set_vertex_attribute(self.id, "fontfamily", fontfamily)
    if fontsize != None:
      self.U.server.ubigraph.set_vertex_attribute(self.id, "fontsize", str(fontsize))
    if visible != None:
      self.U.server.ubigraph.set_vertex_attribute(self.id, "visible", str(visible))
    if callback != None:
      self.U.server.ubigraph.set_vertex_attribute(self.id, "callback_left_doubleclick", 
        callback)

  def destroy(self):
    self.U.server.ubigraph.remove_vertex(self.id)



class Edge:
  def __init__(self, U, x, y, id=None, style=None, arrow=None, 
             arrow_position=None, arrow_length=None, arrow_radius=None, 
             arrow_reverse=None, color=None,
             label=None, fontcolor=None, fontfamily=None, fontsize=None,
             oriented=None, spline=None, showstrain=None, stroke=None,
             strength=None, visible=None, width=None):
    self.U = U
    if id == None:
      self.id = U.server.ubigraph.new_edge(x.id,y.id)
    else:
      U.server.ubigraph.new_edge_w_id(id,x.id,y.id)
      self.id = id
    self.set(style=style, arrow=arrow, arrow_position=arrow_position, 
      arrow_length=arrow_length, arrow_radius=arrow_radius, color=color,
      label=label, fontcolor=fontcolor, fontfamily=fontfamily,
      fontsize=fontsize, oriented=oriented, spline=spline,
      showstrain=showstrain, stroke=stroke, strength=strength,
      visible=visible, width=width)

  def set(self, style=None, arrow=None, arrow_position=None, 
             arrow_length=None, arrow_radius=None, arrow_reverse=None,  
             color=None, label=None, fontcolor=None, fontfamily=None, 
             fontsize=None, oriented=None, spline=None, showstrain=None, 
             stroke=None, strength=None, visible=None, width=None):
    if style != None:
      self.U.server.ubigraph.change_edge_style(self.id, style.id)
    if arrow != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "arrow", str(arrow))
    if arrow_position != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "arrow_position", 
        str(arrow_position))
    if arrow_length != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "arrow_length",
        str(arrow_length))
    if arrow_radius != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "arrow_radius",
        str(arrow_radius))
    if arrow_reverse != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "arrow_reverse",
        str(arrow_reverse))
    if color != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "color", color)
    if label != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "label", label)
    if fontcolor != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "fontcolor", fontcolor)
    if fontfamily != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "fontfamily", fontfamily)
    if fontsize != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "fontsize", str(fontsize))
    if oriented != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "oriented", str(oriented))
    if spline != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "spline", str(spline))
    if showstrain != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "showstrain", str(showstrain))
    if stroke != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "stroke", stroke)
    if strength != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "strength", str(strength))
    if visible != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "visible", str(visible))
    if width != None:
      self.U.server.ubigraph.set_edge_attribute(self.id, "width", str(width))

  def destroy(self):
    self.U.server.ubigraph.remove_edge(self.id)


class VertexStyle:
  def __init__(self, U, parentStyle=None, id=None, color=None, shape=None,
                label=None, size=None, fontcolor=None, fontfamily=None,
                fontsize=None, visible=None):
    self.U = U
    parentStyle2 = parentStyle
    if parentStyle == None:
      if id == 0:
        # Represent the global default style
        self.id = 0
        return
      else:
        parentStyle2 = U.defaultVertexStyle

    if id == None:
      self.id = U.server.ubigraph.new_vertex_style(parentStyle2.id)
    else:
      U.server.ubigraph.new_vertex_style_w_id(id, parentStyle2.id)
      self.id = id
    self.set(color=color, shape=shape, label=label, size=size,
      fontcolor=fontcolor, fontfamily=fontfamily, fontsize=fontsize, 
      visible=visible)

  def set(self, color=None, shape=None, label=None, size=None, 
      fontcolor=None, fontfamily=None, fontsize=None, visible=None, 
      callback=None): 
    if color != None:
      self.U.server.ubigraph.set_vertex_style_attribute(self.id, "color", color)
    if shape != None:
      self.U.server.ubigraph.set_vertex_style_attribute(self.id, "shape", shape)
    if label != None:
      self.U.server.ubigraph.set_vertex_style_attribute(self.id, "label", label)
    if size != None:
      self.U.server.ubigraph.set_vertex_style_attribute(self.id, "size", str(size))
    if fontcolor != None:
      self.U.server.ubigraph.set_vertex_style_attribute(self.id, "fontcolor", fontcolor)
    if fontfamily != None:
      self.U.server.ubigraph.set_vertex_style_attribute(self.id, "fontfamily", fontfamily)
    if fontsize != None:
      self.U.server.ubigraph.set_vertex_style_attribute(self.id, "fontsize", str(fontsize))
    if visible != None:
      self.U.server.ubigraph.set_vertex_style_attribute(self.id, "visible", str(visible))
    if callback != None:
      self.U.server.ubigraph.set_vertex_style_attribute(self.id, "callback_left_doubleclick", 
        callback)



class EdgeStyle:
  def __init__(self, U, parentStyle=None, id=None, arrow=None, color=None,
             label=None, fontcolor=None, fontfamily=None, fontsize=None,
             oriented=None, spline=None, showstrain=None, stroke=None,
             strength=None, visible=None, width=None):
    self.U = U
    parentStyle2 = parentStyle
    if parentStyle2 == None:
      if id == 0:
        # Represent the global default style
        self.id = 0
        return
      else:
        parentStyle2 = U.defaultEdgeStyle

    if id == None:
      self.id = U.server.ubigraph.new_edge_style(parentStyle2.id)
    else:
      U.server.ubigraph.new_edge_style_w_id(id, parentStyle2.id)
      self.id = id
    self.set(arrow=arrow, color=color, label=label, fontcolor=fontcolor, 
      fontfamily=fontfamily, fontsize=fontsize, oriented=oriented, 
      spline=spline, showstrain=showstrain, stroke=stroke, strength=strength,
      visible=visible, width=width)

  def set(self, arrow=None, color=None,
             label=None, fontcolor=None, fontfamily=None, fontsize=None,
             oriented=None, spline=None, showstrain=None, stroke=None,
             strength=None, visible=None, width=None):
    if arrow != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "arrow", str(arrow))
    if arrow_position != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "arrow_position",
        str(arrow_position))
    if arrow_length != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "arrow_length",
        str(arrow_length))
    if arrow_radius != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "arrow_radius",
        str(arrow_radius))
    if arrow_reverse != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "arrow_reverse",
        str(arrow_reverse))
    if color != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "color", color)
    if label != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "label", label)
    if fontcolor != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "fontcolor", fontcolor)
    if fontfamily != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "fontfamily", fontfamily)
    if fontsize != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "fontsize", str(fontsize))
    if oriented != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "oriented", str(oriented))
    if spline != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "spline", str(spline))
    if showstrain != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "showstrain", str(showstrain))
    if stroke != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "stroke", stroke)
    if strength != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "strength", str(strength))
    if visible != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "visible", str(visible))
    if width != None:
      self.U.server.ubigraph.set_edge_style_attribute(self.id, "width", str(width))


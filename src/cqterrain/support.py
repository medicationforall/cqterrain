import cadquery as cq

def support(length=10, width=10, height=30, inner_height=8, inner_length=4, inner_width=4, top_offset=0):
    result = (cq.Workplane("XY")
          .box(length, width, inner_height)
          .wires(">Z")
          .toPending()
          .workplane(offset=height-inner_height).center(0,(width/2)-(inner_width/2)+(top_offset*-1))
          .rect(inner_length, inner_width)
          .loft(combine=True)
          )

    #zero out result
    result = result.translate((0,0,inner_height/2))
    # center column
    result = result.translate((0,0,-1*(height/2)))
    return result

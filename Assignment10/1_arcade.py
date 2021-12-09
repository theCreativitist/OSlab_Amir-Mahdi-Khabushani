import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110
DIAGONAL_HALF= 7 # nesfe ghotre lozi (for scaling)

arcade.open_window(400, 400, "Complex Loops - Box")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

for row in range(10):
    for column in range(10):
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        a = DIAGONAL_HALF # for simplification
        
        if row%2==0:
            if column%2==0:
                arcade.draw_polygon_filled([[x-a,y],[x,y+a],[x+a,y],[x,y-a]],arcade.color.RED)
            else:
                arcade.draw_polygon_filled([[x-a,y],[x,y+a],[x+a,y],[x,y-a]],arcade.color.BLUE)
        else:
            if column%2==0:
                arcade.draw_polygon_filled([[x-a,y],[x,y+a],[x+a,y],[x,y-a]],arcade.color.BLUE)
            else:
                arcade.draw_polygon_filled([[x-a,y],[x,y+a],[x+a,y],[x,y-a]],arcade.color.RED)
        
arcade.finish_render()
arcade.run()

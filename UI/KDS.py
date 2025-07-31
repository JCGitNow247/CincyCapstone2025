#Import TruckBytes Standard UI options
from OurDisplay import *

# variables
CARD_WIDTH = 150
CARD_HEIGHT = 160
CARD_PADDING = 10
MAX_WIDTH = 950

# Create canvas to allow dynamic vertical space
canvas = Canvas(Window, width=MAX_WIDTH, height=600)
canvas.pack(side="left", fill="both", expand=True)

# Creates a scrollbar for KDS
scrollbar = Scrollbar(Window, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Frame inside canvas where cards will be placed
order_frame = CTkFrame(canvas, width=MAX_WIDTH)
canvas.create_window((0, 0), window=order_frame, anchor="nw")

# Creates order cards of a KDS
def create_order_card():
    for widget in order_frame.winfo_children():
        widget.destroy()

    orders = example_orders

    x = y = 0
    row_height = 0

    for index, order in enumerate(orders):
        card = CTkFrame(order_frame, width=CARD_WIDTH, height=CARD_HEIGHT, corner_radius=10, border_width=1, border_color="gray")
        card.place(x=x, y=y)

        CTkLabel(card, text=f"Order #{order['id']}", font=('Arial', 14, 'bold')).pack(anchor="w", padx=6, pady=(4, 2))

        for item in order["order"]:
            CTkLabel(card, text=f"• {item['name']} - ${item['price']:.2f}", font=('Arial', 12)).pack(anchor="w", padx=10)
            for sub in item["items"]:
                CTkLabel(card, text=f"   - {sub['name']}", font=('Arial', 10)).pack(anchor="w", padx=20)

        Window.update_idletasks()  # Allow layout to calculate height
        card_height = card.winfo_height()

        x += CARD_WIDTH + CARD_PADDING
        row_height = max(row_height, card_height)

        if x + CARD_WIDTH > MAX_WIDTH:
            x = 0
            y += row_height + CARD_PADDING
            row_height = 0


    # Adjust scrollable area height dynamically
    total_height = y + row_height + CARD_PADDING
    order_frame.configure(height=total_height)
    canvas.configure(scrollregion=(0, 0, MAX_WIDTH, total_height))



example_orders = [
    {
        "id": 1,
        "order": [
            {"name": "Burger", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Tomato"}, {"name": "Mayo"}]},
            {"name": "Fries", "price": 1.50, "items": []},
            {"name": "Coke", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
    {
        "id": 2,
        "order": [
            {"name": "Hotdog", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Mustard"}, {"name": "Ketchup"}]},
            {"name": "Burger", "price": 1.50, "items": []},
            {"name": "Sprite", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
    {
        "id": 3,
        "order": [
            {"name": "Hotdog", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Mustard"}, {"name": "Ketchup"}]},
            {"name": "Burger", "price": 1.50, "items": []},
            {"name": "Sprite", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
        {
        "id": 4,
        "order": [
            {"name": "Hotdog", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Mustard"}, {"name": "Ketchup"}]},
            {"name": "Burger", "price": 1.50, "items": []},
            {"name": "Sprite", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
    {
        "id": 5,
        "order": [
            {"name": "Burger", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Tomato"}, {"name": "Mayo"}]},
            {"name": "Fries", "price": 1.50, "items": []},
            {"name": "Coke", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
    {
        "id": 6,
        "order": [
            {"name": "Hotdog", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Mustard"}, {"name": "Ketchup"}]},
            {"name": "Burger", "price": 1.50, "items": []},
            {"name": "Sprite", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
    {
        "id": 7,
        "order": [
            {"name": "Hotdog", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Mustard"}, {"name": "Ketchup"}]},
            {"name": "Burger", "price": 1.50, "items": []},
            {"name": "Sprite", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
        {
        "id": 8,
        "order": [
            {"name": "Hotdog", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Mustard"}, {"name": "Ketchup"}]},
            {"name": "Burger", "price": 1.50, "items": []},
            {"name": "Sprite", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
        {
        "id": 1,
        "order": [
            {"name": "Burger", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Tomato"}, {"name": "Mayo"}]},
            {"name": "Fries", "price": 1.50, "items": []},
            {"name": "Coke", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
    {
        "id": 2,
        "order": [
            {"name": "Hotdog", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Mustard"}, {"name": "Ketchup"}]},
            {"name": "Burger", "price": 1.50, "items": []},
            {"name": "Sprite", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
    {
        "id": 3,
        "order": [
            {"name": "Hotdog", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Mustard"}, {"name": "Ketchup"}]},
            {"name": "Burger", "price": 1.50, "items": []},
            {"name": "Sprite", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
    {
        "id": 4,
        "order": [
            {"name": "Hotdog", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Mustard"}, {"name": "Ketchup"}]},
            {"name": "Burger", "price": 1.50, "items": []},
            {"name": "Sprite", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
    {
        "id": 5,
        "order": [
            {"name": "Burger", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Tomato"}, {"name": "Mayo"}]},
            {"name": "Fries", "price": 1.50, "items": []},
            {"name": "Coke", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
    {
        "id": 6,
        "order": [
            {"name": "Hotdog", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Mustard"}, {"name": "Ketchup"}]},
            {"name": "Burger", "price": 1.50, "items": []},
            {"name": "Sprite", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
    {
        "id": 7,
        "order": [
            {"name": "Hotdog", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Mustard"}, {"name": "Ketchup"}]},
            {"name": "Burger", "price": 1.50, "items": []},
            {"name": "Sprite", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
    {
        "id": 8,
        "order": [
            {"name": "Hotdog", "price": 9.50, "items": [{"name": "Lettuce"}, {"name": "Mustard"}, {"name": "Ketchup"}]},
            {"name": "Burger", "price": 1.50, "items": []},
            {"name": "Sprite", "price": 1.50, "items": [{"name": "Bottle"}]},
        ]
    },
]


#Intantiate UI options
Create_Window()
Create_Menubar()

#Intantiate UI specific to this page
create_order_card()



#Create mainloop to run program
Window.mainloop()
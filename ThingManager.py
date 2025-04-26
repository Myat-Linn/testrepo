import csv
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText

class ThingManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.headers = ["id", "name", "type", "color", "weight", "price", "age", "description"]
        # Create the file with headers if it doesn't exist
        if not os.path.exists(file_path):
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
            # Add sample data
            self.add_sample_data()
    
    def add_sample_data(self):
        sample_data = [
            [1, "iPhone 14 Pro", "Mobile Phone", "Silver", "206g", 999.99, 1, "Apple's flagship smartphone"],
            [2, "Golden Retriever", "Animal", "Golden", "70kg", 1200.00, 3, "Friendly family dog breed"],
            [3, "Tesla Model 3", "Car", "Red", "1800kg", 42990.00, 2, "Electric sedan with autopilot"],
            [4, "Interstellar", "Movie", "N/A", "N/A", 19.99, 9, "Sci-fi space exploration film"],
            [5, "Bohemian Rhapsody", "Music", "N/A", "N/A", 1.29, 48, "Queen's iconic song"],
            [6, "Soccer", "Sport", "N/A", "450g", 25.00, 150, "Ball game with two teams of 11 players"],
            [7, "Beach House", "House", "White", "N/A", 850000.00, 5, "Vacation property near the ocean"],
            [8, "Mickey Mouse", "Cartoon", "Black/Red", "N/A", 0.00, 95, "Disney's iconic character"],
            [9, "Eiffel Tower", "Tourist Attraction", "Iron-colored", "10100 tons", 25.00, 134, "Famous Paris landmark"],
            [10, "MacBook Pro", "Computer", "Space Gray", "2kg", 1999.99, 1, "Apple laptop for professionals"],
            [11, "Sony PlayStation 5", "Gaming Console", "White", "4.5kg", 499.99, 3, "Next-gen gaming console with ray tracing"],
            [12, "Bengal Cat", "Animal", "Spotted Brown", "6kg", 1800.00, 2, "Domestic cat with wild appearance"],
            [13, "Jeep Wrangler", "Car", "Black", "1950kg", 32995.00, 1, "Off-road 4x4 vehicle with removable top"],
            [14, "The Shawshank Redemption", "Movie", "N/A", "N/A", 14.99, 29, "Prison drama based on Stephen King novella"],
            [15, "Stairway to Heaven", "Music", "N/A", "N/A", 1.99, 52, "Led Zeppelin's iconic rock ballad"],
            [16, "Basketball", "Sport", "Orange", "620g", 29.99, 130, "Team sport with two hoops and ten players"],
            [17, "Modern Loft", "House", "Gray", "N/A", 420000.00, 3, "Open concept city apartment with industrial design"],
            [18, "SpongeBob SquarePants", "Cartoon", "Yellow", "N/A", 0.00, 24, "Animated series about a sponge living in Bikini Bottom"],
            [19, "Great Wall of China", "Tourist Attraction", "Gray/Tan", "Unknown", 20.00, 2300, "Ancient defensive wall spanning thousands of miles"],
            [20, "Bose QuietComfort Earbuds", "Electronics", "Black", "8.5g", 279.99, 2, "Wireless noise-cancelling earbuds"],
            [21, "Aloe Vera Plant", "Plant", "Green", "1.5kg", 15.99, 1, "Succulent plant with medicinal properties"],
            [22, "Harry Potter Series", "Book", "Various", "3.5kg", 120.00, 26, "Fantasy novel series by J.K. Rowling"],
            [23, "Rolex Submariner", "Watch", "Silver/Blue", "150g", 9995.00, 3, "Luxury diving watch with date display"],
            [24, "Adidas Ultraboost", "Footwear", "White", "310g", 180.00, 1, "Running shoes with responsive cushioning"],
            [25, "Chocolate Cake", "Food", "Brown", "1.2kg", 28.99, 0, "Sweet dessert with chocolate frosting"],
            [26, "Yoga", "Exercise", "N/A", "N/A", 15.00, 5000, "Physical practice focusing on strength and flexibility"],
            [27, "WordPress", "Software", "N/A", "N/A", 0.00, 19, "Content management system for websites"],
            [28, "Amazon Echo Dot", "Smart Device", "Black", "340g", 49.99, 2, "Voice-controlled smart speaker with Alexa"],
            [29, "Niagara Falls", "Natural Wonder", "Blue", "N/A", 0.00, 12000, "Massive waterfall on US-Canada border"],
            [30, "Monopoly", "Board Game", "Multi-colored", "860g", 19.99, 87, "Property trading board game"]
        ]
        
        for item in sample_data:
            with open(self.file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(item)
    
    def get_all_data(self):
        data = []
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                headers = next(reader)  # Skip the header row
                for row in reader:
                    data.append(row)
        except Exception as e:
            print(f"Error reading file: {e}")
        return data
    
    def add_data(self, data):
        # Find the next ID
        next_id = 1
        all_data = self.get_all_data()
        if all_data:
            max_id = max([int(item[0]) for item in all_data if item[0].isdigit()])
            next_id = max_id + 1
        
        data.insert(0, next_id)  # Add ID at the beginning
        
        try:
            with open(self.file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
            return True
        except Exception as e:
            print(f"Error adding data: {e}")
            return False
    
    def search_data(self, query, field):
        results = []
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                headers = next(reader)  # Skip the header row
                field_index = self.headers.index(field.lower()) if field.lower() in self.headers else 1  # Default to name
                
                for row in reader:
                    if query.lower() in row[field_index].lower():
                        results.append(row)
        except Exception as e:
            print(f"Error searching data: {e}")
        return results
    
    def delete_data(self, id_to_delete):
        all_data = self.get_all_data()
        updated_data = [row for row in all_data if row[0] != str(id_to_delete)]
        
        if len(updated_data) == len(all_data):
            return False  # No item was deleted
        
        try:
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
                writer.writerows(updated_data)
            return True
        except Exception as e:
            print(f"Error deleting data: {e}")
            return False
    
    def update_data(self, id_to_update, updated_data):
        all_data = self.get_all_data()
        updated = False
        
        for i, row in enumerate(all_data):
            if row[0] == str(id_to_update):
                updated_data.insert(0, id_to_update)  # Make sure ID is preserved
                all_data[i] = updated_data
                updated = True
                break
        
        if updated:
            try:
                with open(self.file_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(self.headers)
                    writer.writerows(all_data)
                return True
            except Exception as e:
                print(f"Error updating data: {e}")
        
        return False


class ThingManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Thing Manager")
        self.geometry("900x600")
        self.configure(padx=10, pady=10)
        
        self.manager = ThingManager("things_data.csv")
        
        self.create_widgets()
        self.refresh_table()
    
    def create_widgets(self):
        # Create tabs
        self.tab_control = ttk.Notebook(self)
        
        self.tab_view = ttk.Frame(self.tab_control)
        self.tab_add = ttk.Frame(self.tab_control)
        self.tab_search = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.tab_view, text="View All Data")
        self.tab_control.add(self.tab_add, text="Add New Data")
        self.tab_control.add(self.tab_search, text="Search Data")
        
        self.tab_control.pack(expand=1, fill="both")
        
        # Create widgets for View tab
        self.view_frame = ttk.Frame(self.tab_view)
        self.view_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Create treeview for data display
        self.tree = ttk.Treeview(self.view_frame, columns=tuple(self.manager.headers), show="headings")
        
        # Define column headings
        for header in self.manager.headers:
            self.tree.heading(header, text=header.capitalize())
            if header == "description":
                self.tree.column(header, width=200)
            elif header == "id":
                self.tree.column(header, width=40)
            else:
                self.tree.column(header, width=100)
        
        self.tree.pack(side=tk.LEFT, fill="both", expand=True)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.view_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Add buttons for edit and delete
        btn_frame = ttk.Frame(self.tab_view)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Edit Selected", command=self.edit_selected).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_selected).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Refresh", command=self.refresh_table).pack(side=tk.LEFT, padx=5)
        
        # Create widgets for Add tab
        add_frame = ttk.LabelFrame(self.tab_add, text="Add New Thing")
        add_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Create form fields
        self.add_entries = {}
        
        for i, header in enumerate(self.manager.headers[1:]):  # Skip ID as it's auto-generated
            ttk.Label(add_frame, text=f"{header.capitalize()}:").grid(row=i, column=0, padx=5, pady=5, sticky="w")
            entry = ttk.Entry(add_frame, width=50)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            self.add_entries[header] = entry
        
        ttk.Button(add_frame, text="Add New Thing", command=self.add_new_thing).grid(row=len(self.manager.headers), column=0, columnspan=2, pady=20)
        
        # Create widgets for Search tab
        search_frame = ttk.LabelFrame(self.tab_search, text="Search Things")
        search_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        ttk.Label(search_frame, text="Search Field:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.search_field = ttk.Combobox(search_frame, values=["Name", "Type"], state="readonly")
        self.search_field.current(0)
        self.search_field.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(search_frame, text="Search Query:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.search_query = ttk.Entry(search_frame, width=50)
        self.search_query.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(search_frame, text="Search", command=self.search_things).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Results area
        ttk.Label(search_frame, text="Search Results:").grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
        
        self.results_frame = ttk.Frame(search_frame)
        self.results_frame.grid(row=4, column=0, columnspan=2, sticky="nsew")
        
        self.search_tree = ttk.Treeview(self.results_frame, columns=tuple(self.manager.headers), show="headings")
        
        # Define column headings for search results
        for header in self.manager.headers:
            self.search_tree.heading(header, text=header.capitalize())
            if header == "description":
                self.search_tree.column(header, width=200)
            elif header == "id":
                self.search_tree.column(header, width=40)
            else:
                self.search_tree.column(header, width=100)
        
        self.search_tree.pack(side=tk.LEFT, fill="both", expand=True)
        
        # Add scrollbar for search results
        search_scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.search_tree.yview)
        search_scrollbar.pack(side=tk.RIGHT, fill="y")
        self.search_tree.configure(yscrollcommand=search_scrollbar.set)
    
    def refresh_table(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Load data from file
        data = self.manager.get_all_data()
        for row in data:
            self.tree.insert("", "end", values=row)
    
    def add_new_thing(self):
        # Get values from entries
        new_data = []
        for header in self.manager.headers[1:]:  # Skip ID
            value = self.add_entries[header].get()
            new_data.append(value)
        
        # Validate data (basic validation)
        if not new_data[0]:  # Name is required
            messagebox.showerror("Error", "Name is required")
            return
        
        # Add the data
        if self.manager.add_data(new_data):
            messagebox.showinfo("Success", "New thing added successfully")
            # Clear the form
            for entry in self.add_entries.values():
                entry.delete(0, tk.END)
            # Refresh the data view
            self.refresh_table()
        else:
            messagebox.showerror("Error", "Failed to add new thing")
    
    def search_things(self):
        query = self.search_query.get()
        field = self.search_field.get()
        
        if not query:
            messagebox.showinfo("Info", "Please enter a search query")
            return
        
        # Map field name to the actual column name
        field_map = {"Name": "name", "Type": "type"}
        field_name = field_map.get(field, "name")
        
        # Clear existing search results
        for item in self.search_tree.get_children():
            self.search_tree.delete(item)
        
        # Perform search
        results = self.manager.search_data(query, field_name)
        
        # Display results
        for row in results:
            self.search_tree.insert("", "end", values=row)
        
        if not results:
            messagebox.showinfo("Search Results", "No matching items found")
    
    def edit_selected(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Please select an item to edit")
            return
        
        # Get the data of the selected item
        item_data = self.tree.item(selected_item, "values")
        if not item_data:
            return
        
        # Create a dialog for editing
        edit_window = tk.Toplevel(self)
        edit_window.title("Edit Thing")
        edit_window.geometry("500x400")
        edit_window.configure(padx=10, pady=10)
        
        # Create form fields
        edit_entries = {}
        
        for i, header in enumerate(self.manager.headers):
            ttk.Label(edit_window, text=f"{header.capitalize()}:").grid(row=i, column=0, padx=5, pady=5, sticky="w")
            entry = ttk.Entry(edit_window, width=50)
            entry.insert(0, item_data[i])
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            
            # Make ID read-only
            if header == "id":
                entry.configure(state="readonly")
            
            edit_entries[header] = entry
        
        # Save button
        def save_edit():
            # Get values from entries
            updated_data = []
            for header in self.manager.headers[1:]:  # Skip ID
                value = edit_entries[header].get()
                updated_data.append(value)
            
            # Update the data
            if self.manager.update_data(item_data[0], updated_data):
                messagebox.showinfo("Success", "Item updated successfully")
                edit_window.destroy()
                self.refresh_table()
            else:
                messagebox.showerror("Error", "Failed to update item")
        
        ttk.Button(edit_window, text="Save Changes", command=save_edit).grid(row=len(self.manager.headers), column=0, columnspan=2, pady=20)
    
    def delete_selected(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Please select an item to delete")
            return
        
        # Get the ID of the selected item
        item_data = self.tree.item(selected_item, "values")
        if not item_data:
            return
        
        # Confirm deletion
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {item_data[1]}?")
        if not confirm:
            return
        
        # Delete the item
        if self.manager.delete_data(item_data[0]):
            messagebox.showinfo("Success", "Item deleted successfully")
            self.refresh_table()
        else:
            messagebox.showerror("Error", "Failed to delete item")


if __name__ == "__main__":
    app = ThingManagerApp()
    app.mainloop()
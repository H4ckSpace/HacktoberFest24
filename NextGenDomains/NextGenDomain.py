import tkinter as tk
from tkinter import ttk, scrolledtext
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import random
import json
from typing import List, Dict
import pyperclip
from PIL import Image, ImageTk
import customtkinter as ctk

class ModernDomainGeneratorGUI:
    def __init__(self):
        # Initialize the main window with custom styling
        self.root = ctk.CTk()
        self.root.title("Futuristic Domain Generator")
        self.root.geometry("1200x800")
        
        # Set the color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Initialize the domain generator
        self.generator = FuturisticDomainGenerator()
        
        self._create_gui_elements()
        
    def _create_gui_elements(self):
        # Create main container
        main_container = ctk.CTkFrame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title Label with modern styling
        title_label = ctk.CTkLabel(
            main_container,
            text="Futuristic Domain Generator",
            font=("Helvetica", 24, "bold")
        )
        title_label.pack(pady=(0, 20))
        
        # Create left panel for controls
        left_panel = ctk.CTkFrame(main_container)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))
        
        # Category Selection
        category_frame = ctk.CTkFrame(left_panel)
        category_frame.pack(fill=tk.X, pady=(0, 10), padx=10)
        
        ctk.CTkLabel(
            category_frame,
            text="Select Category:",
            font=("Helvetica", 12)
        ).pack(pady=(5, 0))
        
        self.category_var = tk.StringVar(value="tech")
        categories = list(self.generator.categories.keys())
        
        self.category_menu = ctk.CTkOptionMenu(
            category_frame,
            values=categories,
            variable=self.category_var,
            command=self._on_category_change
        )
        self.category_menu.pack(fill=tk.X, pady=5)
        
        # Number of domains
        count_frame = ctk.CTkFrame(left_panel)
        count_frame.pack(fill=tk.X, pady=(0, 10), padx=10)
        
        ctk.CTkLabel(
            count_frame,
            text="Number of Domains:",
            font=("Helvetica", 12)
        ).pack(pady=(5, 0))
        
        self.count_var = tk.StringVar(value="5")
        count_entry = ctk.CTkEntry(
            count_frame,
            textvariable=self.count_var
        )
        count_entry.pack(fill=tk.X, pady=5)
        
        # Generate Button
        self.generate_btn = ctk.CTkButton(
            left_panel,
            text="Generate Domains",
            command=self._generate_domains,
            height=40
        )
        self.generate_btn.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # Create right panel for results
        right_panel = ctk.CTkFrame(main_container)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Results Area
        self.results_text = ctk.CTkTextbox(
            right_panel,
            wrap=tk.WORD,
            font=("Courier", 12)
        )
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Copy Button
        self.copy_btn = ctk.CTkButton(
            right_panel,
            text="Copy All Domains",
            command=self._copy_to_clipboard,
            height=40
        )
        self.copy_btn.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # Status Bar
        self.status_var = tk.StringVar()
        self.status_bar = ctk.CTkLabel(
            main_container,
            textvariable=self.status_var,
            font=("Helvetica", 10)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def _generate_domains(self):
        try:
            count = int(self.count_var.get())
            if count <= 0 or count > 50:
                self.status_var.set("Please enter a number between 1 and 50")
                return
                
            category = self.category_var.get()
            domains = self.generator.generate_name(category, count)
            
            # Clear previous results
            self.results_text.delete("1.0", tk.END)
            
            # Display new results with custom formatting
            self.results_text.insert("1.0", "Generated Domains:\n\n")
            for i, domain in enumerate(domains, 1):
                self.results_text.insert(tk.END, f"{i}. {domain}\n")
                
            self.status_var.set(f"Successfully generated {count} domains for {category} category")
            
        except ValueError as e:
            self.status_var.set("Please enter a valid number")
            
    def _copy_to_clipboard(self):
        text = self.results_text.get("1.0", tk.END)
        pyperclip.copy(text)
        self.status_var.set("All domains copied to clipboard!")
        
    def _on_category_change(self, event):
        self.status_var.set(f"Selected category: {self.category_var.get()}")
        
    def run(self):
        self.root.mainloop()

class FuturisticDomainGenerator:
    def __init__(self):
        self.categories = {
            'tech': {
                'prefixes': ['cyber', 'quantum', 'neo', 'hyper', 'meta', 'digi', 'tech', 'ai', 'smart', 'sync'],
                'suffixes': ['verse', 'flux', 'nova', 'sync', 'labs', 'tech', 'hub', 'net', 'cloud', 'core'],
                'modifiers': ['pro', 'plus', 'prime', 'next', 'max', 'ultra', 'elite'],
            },
            'finance': {
                'prefixes': ['fin', 'crypto', 'block', 'wealth', 'cap', 'trade', 'pay', 'cash', 'bank', 'coin'],
                'suffixes': ['wealth', 'capital', 'fin', 'trade', 'invest', 'money', 'trust', 'asset', 'bank'],
                'modifiers': ['pro', 'global', 'smart', 'secure', 'prime', 'direct'],
            },
            'healthcare': {
                'prefixes': ['med', 'health', 'care', 'bio', 'life', 'vital', 'cure', 'heal', 'doc', 'pulse'],
                'suffixes': ['health', 'care', 'med', 'life', 'clinic', 'pharma', 'wellness', 'therapy'],
                'modifiers': ['plus', 'pro', 'care', 'direct', 'connect'],
            },
            'education': {
                'prefixes': ['edu', 'learn', 'skill', 'mind', 'brain', 'know', 'teach', 'study', 'academy'],
                'suffixes': ['learn', 'edu', 'mind', 'skill', 'academy', 'class', 'school', 'hub'],
                'modifiers': ['plus', 'pro', 'max', 'genius', 'smart'],
            },
            'ecommerce': {
                'prefixes': ['shop', 'buy', 'store', 'mart', 'market', 'retail', 'trade', 'deal', 'sale'],
                'suffixes': ['cart', 'mart', 'shop', 'store', 'market', 'buy', 'mall', 'zone'],
                'modifiers': ['pro', 'plus', 'max', 'direct', 'prime', 'express'],
            },
            'entertainment': {
                'prefixes': ['fun', 'play', 'joy', 'live', 'stream', 'media', 'watch', 'cast', 'view'],
                'suffixes': ['play', 'fun', 'joy', 'media', 'cast', 'stream', 'show', 'live'],
                'modifiers': ['plus', 'pro', 'max', 'prime', 'ultra'],
            },
            'gaming': {
                'prefixes': ['game', 'play', 'level', 'pixel', 'byte', 'quest', 'arena', 'nexus', 'epic'],
                'suffixes': ['game', 'play', 'verse', 'world', 'zone', 'realm', 'hub', 'arena'],
                'modifiers': ['pro', 'max', 'ultra', 'elite', 'prime'],
            }
        }
        
        self.tlds = {
            'tech': ['.io', '.tech', '.ai', '.app', '.dev', '.network'],
            'finance': ['.finance', '.bank', '.capital', '.invest', '.money', '.trade'],
            'healthcare': ['.health', '.care', '.medical', '.clinic', '.pharmacy'],
            'education': ['.edu', '.academy', '.school', '.learning', '.study'],
            'ecommerce': ['.shop', '.store', '.market', '.buy', '.deals'],
            'entertainment': ['.media', '.live', '.stream', '.show', '.fun'],
            'gaming': ['.game', '.play', '.zone', '.gg', '.world']
        }
        
        self.common_tlds = ['.com', '.net', '.co', '.xyz']

    def generate_name(self, category: str, count: int = 1) -> List[str]:
        if category not in self.categories:
            raise ValueError(f"Category '{category}' not found")
        
        generated_names = set()
        while len(generated_names) < count:
            cat_elements = self.categories[category]
            
            prefix = random.choice(cat_elements['prefixes'])
            suffix = random.choice(cat_elements['suffixes'])
            
            patterns = [
                lambda: f"{prefix}{suffix}",
                lambda: f"{prefix}-{suffix}",
                lambda: f"{prefix}{random.choice(cat_elements['modifiers'])}{suffix}",
                lambda: f"{prefix}{random.randint(1, 999)}",
                lambda: f"{prefix}{suffix}{random.randint(1, 99)}",
            ]
            
            base_name = random.choice(patterns)()
            specific_tlds = self.tlds.get(category, [])
            all_tlds = specific_tlds + self.common_tlds
            tld = random.choice(all_tlds)
            
            domain = f"{base_name}{tld}".lower()
            if domain not in generated_names:
                generated_names.add(domain)
        
        return list(generated_names)

if __name__ == "__main__":
    app = ModernDomainGeneratorGUI()
    app.run()

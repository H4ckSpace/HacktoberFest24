const meals = [
    {
      name: "Spaghetti Carbonara",
      restaurant: "Italian Restaurant",
      price: "$5.99",
      image: "https://example.com/meal1.jpg",
    },
    {
      name: "Chicken Burrito",
      restaurant: "Mexican Delight",
      price: "$4.50",
      image: "https://example.com/meal2.jpg",
    },
    {
      name: "Vegan Salad",
      restaurant: "Green Bistro",
      price: "$3.99",
      image: "https://example.com/meal3.jpg",
    },
    {
      name: "Cheeseburger",
      restaurant: "Burger Town",
      price: "$2.99",
      image: "https://example.com/meal4.jpg",
    },
  ];
  
  // Load meals into the page
  window.onload = () => {
    const mealsContainer = document.getElementById("mealsContainer");
    meals.forEach((meal) => {
      const mealItem = document.createElement("div");
      mealItem.classList.add("meal-item");
  
      mealItem.innerHTML = `
        <img src="${meal.image}" alt="${meal.name}">
        <h3>${meal.name}</h3>
        <p>${meal.restaurant}</p>
        <p class="price">${meal.price}</p>
      `;
      mealsContainer.appendChild(mealItem);
    });
  };
  
  // Search functionality (basic)
  function searchRestaurants() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const mealsContainer = document.getElementById("mealsContainer");
    mealsContainer.innerHTML = ''; // Clear previous meals
  
    const filteredMeals = meals.filter(
      (meal) =>
        meal.name.toLowerCase().includes(query) ||
        meal.restaurant.toLowerCase().includes(query)
    );
  
    if (filteredMeals.length === 0) {
      mealsContainer.innerHTML = '<p>No meals found.</p>';
    } else {
      filteredMeals.forEach((meal) => {
        const mealItem = document.createElement("div");
        mealItem.classList.add("meal-item");
  
        mealItem.innerHTML = `
          <img src="${meal.image}" alt="${meal.name}">
          <h3>${meal.name}</h3>
          <p>${meal.restaurant}</p>
          <p class="price">${meal.price}</p>
        `;
        mealsContainer.appendChild(mealItem);
      });
    }
  }
  
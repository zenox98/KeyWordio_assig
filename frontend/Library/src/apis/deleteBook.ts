import axios from 'axios';

export const updateBook = async (id: string, updatedBookData: any) => { // Use a more specific type than 'any' if possible
  try {
    const response = await axios.put(`http://localhost:8000/delete_book/${id}`, updatedBookData); // Replace with your API
    return response.data;
  } catch (error) {
      console.error("API Error:", error);
      throw error;
  }
};

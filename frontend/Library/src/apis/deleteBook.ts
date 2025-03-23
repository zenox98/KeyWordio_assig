import axios from 'axios';

export const deleteBook = async (id: string) => {
  try {
    const response = await axios.delete(`${import.meta.env.VITE_URL}/delete_book/${id}`); // Replace with your API endpoint
    return response.data; // Or just return response if you don't need the data
  } catch (error) {
    console.error("API Error:", error);
    throw error; // Re-throw the error so the calling function can handle it
  }
};

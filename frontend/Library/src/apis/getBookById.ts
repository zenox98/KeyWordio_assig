import axios from 'axios';
import { booksInfoProps } from '../types/book';

export const getBookById = async (id: string): Promise<booksInfoProps> => {
  try {
    const response = await axios.get<booksInfoProps>(`http://localhost:8000/get_book_by_id/${id}`);
    return response.data;
  } catch (error) {
    console.error('API Error:', error);
    throw error; // Re-throw for component to handle
  }
};

import axios from "axios";
import { booksInfoProps } from "../types/book";

export const postAddBook = async (data: booksInfoProps) => {
  try {
    const response = await axios.post(
      `${import.meta.env.VITE_URL}/library/add_book/`,
      data,
      { 
        headers : {
          "Content-Type": "application/json"
        }
      }
    );
    console.log(data)
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

import axios from "axios";

// function to get data with method 
export const getAllBooks = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/library/list_books`)
    return response.data
  } catch (error) {
    console.log(error)
    return error
  }
}

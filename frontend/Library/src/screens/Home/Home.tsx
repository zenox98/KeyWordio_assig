import { useState, useEffect } from "react";
import { getAllBooks } from "../../apis/getAllBooks";
import { deleteBook } from "../../apis/deleteBook";

// types
import { booksInfoProps, booksInfoProps2 } from "../../types/book";
import { Link, useNavigate } from "react-router";

export default function Home() {
  const [listOfBooks, setListOfBooks] = useState<booksInfoProps2[]>([]);
  
  const navigate = useNavigate();

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        const data: booksInfoProps[] = await getAllBooks();
        if (Array.isArray(data)) {
          console.log(data);
          const url = "http://localhost:8000";
          const listData: booksInfoProps2[] = [];
          data.map((item: booksInfoProps) => {
            listData.push({
              book_id: item.book_id,
              book_name: item.book_name,
              book_image: `${url}${item.images[0].image}`,
              book_price: item.book_price,
              book_author: item.book_author,
              book_description: item.book_description,
              book_created_at: item.book_created_at,
              book_updated_at: item.book_updated_at,
            });
          });
          console.log(listData);
          setListOfBooks(listData);
        } else {
          console.error("Unexpected response format:", data);
          setListOfBooks([]); // Ensure it's always an array
        }
      } catch (error) {
        console.error("Error fetching books:", error);
        setListOfBooks([]); // Fallback to an empty array on failure
      }
    };
    fetchBooks();
  }, []);

  const handleDelete = async (id: string) => {
    try {
      await deleteBook(id); // Call the delete API
      setListOfBooks(listOfBooks.filter((book) => book.book_id !== id)); // Update the state
       //Optional Refetch:  fetchBooks(); // Or re-fetch the books (less efficient)
    } catch (error) {
      console.error("Error deleting book:", error);
    }
  };

  const handleUpdate = (id: string) => {
    navigate(`/update/${id}`);
  };

  return (
    <div className=" p-5 w-full h-screen flex flex-wrap justify-center items-center">
      <div className="border border-black p-2 w-full h-full">
        <div className="w-full h-auto px-1 py-3 mx-1">
          <Link to="/add">
            <button className="border border-black p-1">Add Book</button>
          </Link>
        </div>

        <table className="w-full h-auto border border-b-gray-700">
          <thead className="w-full h-auto">
            <tr className="">
              <th className="border border-black">Book Name</th>
              <th className="border border-black">Book Author</th>
              <th className="border border-black">Book Image</th>
              <th className="border border-black">Book Price</th>
              <th className="border border-black">Book description</th>
              <th className="border border-black">created at</th>
              <th className="border border-black">updated at</th>
              <th className="border border-black">delete book</th>
              <th className="border border-black">update book</th>
            </tr>
          </thead>
          <tbody className="w-full h-auto">
            {listOfBooks.map((item: booksInfoProps2) => (
              <tr className="border-b border-b-black">
                <td className="pl-2">{item.book_name}</td>
                <td className="pl-2">{item.book_author}</td>
                <td className="pl-2 w-56 h-auto">
                  <img
                    className="w-fit p-1 h-auto"
                    src={item.book_image}
                    alt={item.book_name}
                  />
                </td>
                <td className="pl-2">{item.book_price}</td>
                <td className="pl-2">{item.book_description}</td>
                <td className="pl-2">{item.book_created_at}</td>
                <td className="pl-2">{item.book_updated_at}</td>
                <td className="pl-2">
                  <button
                    className="p-1 border border-black"
                    onClick={() => handleDelete(item.book_id)}
                  >
                    Delete
                  </button>
                </td>
                <td className="pl-2">
                  <button
                    className="p-1 border border-black"
                    onClick={() => handleUpdate(item.book_id)}
                  >
                    Update
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

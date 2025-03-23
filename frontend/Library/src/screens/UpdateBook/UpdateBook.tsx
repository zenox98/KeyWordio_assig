import { useState } from "react";
import { Link, useNavigate } from "react-router";
import { bookImageProp, booksInfoProps } from "../../types/book";
import { postAddBook } from "../../apis/postAddBook";

interface InputBoxProps {
  value?: string | number;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
  label?: string;
  type: string;
  id: string;
  name?: string;
  placeholder?: string;
  width: string;
  required?: boolean;
}

const InputBox = (props: InputBoxProps) => {
  const {
    value,
    onChange,
    label = "",
    type,
    id,
    name,
    placeholder = "",
    width,
    required = false,
  } = props;

  return (
    <div style={{ width: width }} className="h-auto py-2 my-2">
      <input
        className="outline-none transition-all focus:outline-sky-200 border border-zinc-400 focus:border-2 focus:border-sky-600 w-full h-full px-2 py-3 mb-3 rounded-md"
        value={value}
        onChange={onChange}
        id={id}
        name={name}
        type={type}
        placeholder={placeholder}
        required={required}
      />
      <label htmlFor={id} className="text-black ml-1">
        {label}
      </label>
    </div>
  );
};

export default function UpdateBook() {
  const [book_name, setBookName] = useState<string>("");
  const [book_id, setBookId] = useState<string>("");
  const [book_author, setBookAuthor] = useState<string>("");
  const [book_price, setBookPrice] = useState<number>();
  const [book_description, setBookDescription] = useState<string>("");
  const [book_image, setBookImage] = useState<File | null>(null);

  const navigate = useNavigate();

  const handleUpdate = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const images : bookImageProp[] = []
    images.push({
      image: book_image,
      created_at: `${Date.now}`
    })

    const formData : booksInfoProps = {
      book_name: book_name,
      book_id: book_id,
      book_author: book_author,
      book_description: book_description,
      book_price: book_price,
      images : images
    };

    console.log(formData);
    postAddBook(formData)

    navigate("/");
  };
  return (
    <div>
      <form onSubmit={handleUpdate} method="post">
        <InputBox
          width="350px"
          name={"book name"}
          type={"text"}
          id={"book_name"}
          label={"Book Name"}
          value={book_name}
          onChange={(e) => setBookName(e.target.value)}
          required={true}
        />
        <InputBox
          width="350px"
          name={"book_id"}
          type={"text"}
          id={"book_id"}
          label={"Book Id"}
          value={book_id}
          onChange={(e) => setBookId(e.target.value)}
          required={true}
        />
        <InputBox
          width="350px"
          name={"book author"}
          type={"text"}
          id={"book_author"}
          label={"Book Author"}
          value={book_author}
          onChange={(e) => setBookAuthor(e.target.value)}
          required={true}
        />
        <InputBox
          width="350px"
          name={"book Price"}
          type={"number"}
          id={"book_price"}
          label={"Book Price"}
          
          onChange={(e) => setBookPrice(Number(e.target.value))}
          required={true}
        />
        <InputBox
          width="350px"
          name={"book image"}
          type={"file"}
          id={"book_image"}
          label={"Book Image"}
          onChange={(e) => setBookImage(e.target.files?.[0] || null)}
          required={true}
        />
        <div style={{ width: "350px"}} className="h-auto py-2 my-2">
          <textarea
            value={book_description}
            onChange={(e) => setBookDescription(e.target.value)}
            id="book_description"
            name="book_description"
            className="outline-none transition-all focus:outline-sky-200 border border-zinc-400 focus:border-2 focus:border-sky-600 w-full h-full px-2 py-3 mb-3 rounded-md"
            rows={7}
            cols={10}
          />
          <label htmlFor="book_description" className="text-black ml-1">
            Book Description
          </label>
        </div>

        <input type="submit" value="Add Book" className="p-2 text-lg border cursor-pointe1 border-black" />
      </form>
    </div>
  );
}

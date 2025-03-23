
export interface booksInfoProps2 {
  book_id : string
  book_name: string,
  book_author: string,
  book_image: string,
  book_price: number,
  book_description: string,
  book_created_at: string,
  book_updated_at: string
}

export interface bookImageProp {
  image: File | null,
  created_at: string
}

export interface booksInfoProps {
  book_id : string
  book_name: string,
  book_author: string,
  book_price: number | undefined,
  book_description: string,
  book_created_at: string,
  book_updated_at: string,
  images: bookImageProp[]
}

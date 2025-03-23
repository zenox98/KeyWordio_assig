import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router'
import Home from "./screens/Home/Home.tsx"
import AddBook from './screens/AddBook/AddBook.tsx'
import UpdateBook from './screens/UpdateBook/UpdateBook.tsx'

const route = createBrowserRouter(
  createRoutesFromElements(
    <Route>
      <Route path='/' element={<Home/>} />
      <Route path='/add' element={<AddBook/>} />
      <Route path='/update/:id' element={<UpdateBook />} />
    </Route>
  )
)

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={route} />
  </StrictMode>,
)

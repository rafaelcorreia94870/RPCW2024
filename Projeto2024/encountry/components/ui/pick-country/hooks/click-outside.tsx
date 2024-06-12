import { useEffect, useRef, MutableRefObject } from "react"

const useClickOutside = (
  callback: () => void,
): MutableRefObject<HTMLFormElement | null> => {
  const ref = useRef<HTMLFormElement | null>(null)

  const handleClick = (e: MouseEvent) => {
    if (ref.current && !ref.current.contains(e.target as Node)) {
      callback()
    }
  }

  useEffect(() => {
    document.addEventListener("click", handleClick)
    return () => {
      document.removeEventListener("click", handleClick)
    }
  }, [])

  return ref
}

export default useClickOutside

import { useEffect, useState } from "react"
import useClickOutside from "./hooks/click-outside"
import SearchContent from "./search-content"
import { useDebounce } from "use-debounce"

interface SearchAutocompleteProps {
  onSelect: (name: string) => void // Add onSelect prop
}

const SearchAutocomplete: React.FC<SearchAutocompleteProps> = ({
  onSelect,
}) => {
  const [isExpanded, setIsExpanded] = useState(false)
  const [loading, setLoading] = useState(false)
  const [noData, setNoData] = useState(false)
  const [autocomplete, setAutocomplete] = useState([])
  const [searchParams, setSearchParams] = useState("")
  const [value] = useDebounce(searchParams, 1000)
  const isEmpty = !autocomplete || autocomplete.length === 0

  useEffect(() => {
    const fetchData = async () => {
      if (!searchParams || searchParams.trim() === "") return
      setLoading(true)

      try {
        const res = await fetch(`/api/search?searchTerm=${searchParams}`)
        const data = await res.json()

        const countryInfo = data.map((item: any) => ({
          country: {
            name: item.country.value,
            flag: item.flag.value,
          },
        }))

        if (countryInfo.length === 0) {
          setNoData(true)
        } else {
          setNoData(false)
        }
        setAutocomplete(countryInfo)
      } catch (error) {
        console.log("Something went wrong", error)
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [value, searchParams])

  const collapes = () => {
    setIsExpanded(false)
    setSearchParams("")
    setAutocomplete([])
    setNoData(false)
  }

  const ref = useClickOutside(collapes)

  const expand = () => {
    setIsExpanded(true)
  }

  const handleSelect = (name: string) => {
    setSearchParams(name)
    onSelect(name)
  }

  return (
    <form
      onSubmit={(e) => e.preventDefault()}
      ref={ref}
      className="relative flex h-full w-full flex-col"
    >
      <input
        type="text"
        placeholder="Insert country name... "
        onFocus={expand}
        className="w-full rounded-md border border-foreground px-3 py-2 text-base outline-none focus:ring focus:ring-primary"
        value={searchParams}
        onChange={(e) => setSearchParams(e.target.value)}
      />

      <div
        className={`absolute left-0 right-0 top-full mt-1 max-h-[15rem] w-full rounded-md bg-card shadow-md transition-all duration-300 ${
          isExpanded ? "max-h-[15rem] opacity-100" : "max-h-0 opacity-0"
        } overflow-y-auto scrollbar scrollbar-track-card scrollbar-thumb-muted scrollbar-thumb-rounded-full hover:cursor-pointer hover:scrollbar-thumb-border active:scrollbar-thumb-primary dark:hover:scrollbar-thumb-zinc-700`}
      >
        {loading && (
          <div className="absolute right-4 top-8 -translate-y-1/2">
            <span className="block h-4 w-4 animate-spin rounded-full border-l-2 border-t-2 border-muted-foreground"></span>
          </div>
        )}

        {noData && (
          <div className="mt-6 h-[15rem] overflow-hidden text-center text-base text-muted-foreground">
            <h1>Country not found... 😥</h1>
          </div>
        )}
        {isEmpty && !noData && (
          <div className="mt-6 h-[15rem] overflow-hidden text-center text-base text-muted-foreground">
            <h1>Select a country... 🌍</h1>
          </div>
        )}

        {!isEmpty && (
          <SearchContent
            autocomplete={autocomplete}
            handleSelect={handleSelect}
          />
        )}
      </div>
    </form>
  )
}

export default SearchAutocomplete

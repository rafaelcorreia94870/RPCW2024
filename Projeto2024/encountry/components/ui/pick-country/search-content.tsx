import React from "react"

interface Country {
  name: string
  flag: string
}

interface AutocompleteItem {
  country: Country
}

interface SearchContentProps {
  autocomplete: AutocompleteItem[]
  handleSelect: (name: string) => void
}

const SearchContent: React.FC<SearchContentProps> = ({
  autocomplete,
  handleSelect,
}) => {
  return (
    <div className="py-2">
      <ul>
        {autocomplete.map((data, index) => {
          const { country } = data
          return (
            <li
              key={index}
              className="flex cursor-pointer items-center justify-between rounded-md px-5 py-2 text-muted-foreground transition duration-500 hover:bg-input hover:text-muted-foreground hover:backdrop-blur-none"
              onClick={() => handleSelect(country.name)}
            >
              <div className="flex items-center gap-8">
                {country.flag && (
                  <img
                    src={country.flag}
                    alt={country.name}
                    className="w-[2rem]"
                  />
                )}
                <h2 className="text-lg">{country.name}</h2>
              </div>
            </li>
          )
        })}
      </ul>
    </div>
  )
}

export default SearchContent

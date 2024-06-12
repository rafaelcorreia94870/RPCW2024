import React from "react"
import { Navbar } from "./ui/header/navbar"
import Title from "./ui/header/game-title"
import { ModeToggle } from "./ui/shadcn/mode-toggle"
import { CountryData } from "@/lib/utils"

interface HeaderProps {
  targetCountry?: CountryData | null
}

const Header = ({ targetCountry }: HeaderProps) => {
  return (
    <div className="flex flex-col rounded-b-[3.rem] pb-3">
      <div className="flex flex-col rounded-b-[4rem] bg-primary px-4 py-10 lg:px-10">
        <Title text="ENCOUNTRY" />
      </div>
      <div className="mt-4 flex justify-center space-x-4">
        <Navbar targetCountry={targetCountry} />
        <ModeToggle />
      </div>
    </div>
  )
}

export default Header

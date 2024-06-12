import React from "react"

interface BigTitleProps {
    text: string
    fontSize?: string
    color?: string
}

const Title = ({ text, fontSize, color }: BigTitleProps) => {
    return (
        <h1 className="dark:text-back mb-5 text-center text-6xl md:text-5xl lg:text-[7rem]">
            <span className="font-heading custom-font bg-clip-text font-extrabold tracking-wider text-green-50 drop-shadow-lg">
                {text}
            </span>
        </h1>
    )
}

export default Title

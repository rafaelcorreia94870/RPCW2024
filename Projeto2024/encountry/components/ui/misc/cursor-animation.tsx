import React, { useState } from "react"
import { DotLottieReact } from "@lottiefiles/dotlottie-react"

interface AnimationProps {
  children: React.ReactNode
  source: string
  classes?: string
}

const CursorAnimation: React.FC<AnimationProps> = ({
  children,
  source,
  classes = "",
}) => {
  const [isHovered, setIsHovered] = useState(false)
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 })

  const handleMouseEnter = () => {
    setIsHovered(true)
    console.log(`hovered: ${isHovered}`)
  }

  const handleMouseLeave = () => {
    setIsHovered(false)
  }

  const handleMouseMove = (event: React.MouseEvent<HTMLDivElement>) => {
    const newPosition = { x: event.clientX, y: event.clientY }
    setMousePosition(newPosition)
  }

  return (
    <div
      className={classes}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      onMouseMove={handleMouseMove}
    >
      {children}
      {isHovered && (
        <div
          style={{
            position: "fixed",
            left: mousePosition.x + 40,
            top: mousePosition.y - 35,
            pointerEvents: "none",
            transform: "translate(-50%, -50%)",
            zIndex: 9999,
          }}
        >
          <DotLottieReact src={`./${source}.json`} autoplay loop={false} />
        </div>
      )}
    </div>
  )
}

export default CursorAnimation

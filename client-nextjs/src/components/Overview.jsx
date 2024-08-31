"use client"
import React from "react"
import Link from "next/link"
import { IoIosArrowForward } from "react-icons/io"
import { useRouter } from "next/navigation"

const Overview = ({ item }) => {
    const router = useRouter()
    const { title, number } = item
    return (
        <div
            onClick={() =>
                router.push(
                    `/detail?about=${title}`
                )
            }
            className="flex shadow-md justify-between items-center w-1/4 border rounded-lg p-4"
        >
            <div>
                <div className="text-sm">
                    {title}
                </div>
                <div className="text-3xl font-medium pt-2">
                    {number}
                </div>
            </div>

            <div className="">
                <IoIosArrowForward size={50} />
            </div>
        </div>
    )
}

export default Overview

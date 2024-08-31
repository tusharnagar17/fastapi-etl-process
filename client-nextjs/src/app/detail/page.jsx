import Sidebar from "@/components/Sidebar"
import React from "react"

export default function page({ searchParams }) {
    const { about } = searchParams
    return (
        <div className="flex min-h-screen w-full">
            <Sidebar />
            {/* About section */}
            <div className="w-full">
                <div className="border-2 p-6 px-10 text-lg font-medium">
                    <span className="text-violet-600">
                        Table View
                    </span>
                    <span> </span>/
                    <span> {about}</span>
                </div>
                <div className="m-4 p-4 border h-[80%] border-gray-300 rounded-lg">
                    Table
                </div>
            </div>

            {/* Table View */}
        </div>
    )
}

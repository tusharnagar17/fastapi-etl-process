"use client"
import CustomBarChart from "@/components/CustomBarChart"
import CustomPieChart from "@/components/CustomPieChart"
import Overview from "@/components/Overview"
import Sidebar from "@/components/Sidebar"
import { SERVER_URL } from "@/services"
import React from "react"
import { ColorRing } from "react-loader-spinner"

const data = [
    {
        title: "Previous Month Order",
        number: 3458,
    },
    {
        title: "Order & Payment Received",
        number: 153,
    },
    { title: "Payment Pending", number: 229 },
    {
        title: "Tolerance rate breached",
        number: 3,
    },
    { title: "Return", number: 277 },
    { title: "Negative Payout", number: 666 },
]

const page = () => {
    // const data = dashboardData()

    if (!data) {
        return (
            <div>
                <ColorRing
                    visible={true}
                    height="80"
                    width="80"
                    ariaLabel="color-ring-loading"
                    wrapperStyle={{}}
                    wrapperClass="color-ring-wrapper"
                    colors={[
                        "#e15b64",
                        "#f47e60",
                        "#f8b26a",
                        "#abbd81",
                        "#849b87",
                    ]}
                />
            </div>
        )
    }

    return (
        <div className="flex min-h-screen">
            <Sidebar />
            <div className="">
                <div className="text-center text-3xl text-violet-700 font-semibold my-6">
                    Dashboard
                </div>
                <div className="border w-full m-4 shadow-md">
                    <div className="py-2 flex items-center justify-center">
                        <input
                            type="text"
                            placeholder={"Search"}
                            className="border-2 rounded-xl px-6 py-2"
                        />
                    </div>
                    <div className="flex flex-wrap justify-around gap-4 p-2">
                        {data &&
                            data.map(
                                (item, index) => {
                                    return (
                                        <Overview
                                            key={
                                                index
                                            }
                                            item={
                                                item
                                            }
                                        />
                                    )
                                }
                            )}
                    </div>
                    <div className="flex justify-center gap-4 px-14 py-6">
                        <CustomBarChart />
                        <CustomPieChart />
                    </div>
                </div>
            </div>
        </div>
    )
}

const dashboardData = async () => {
    try {
        const res = await fetch(
            `${SERVER_URL}/dashboard`
        )

        if (!res.ok) {
            return
        }

        return res.json()
    } catch (error) {
        console.log(
            "Error while fetch /dashboard"
        )
    }
}

export default page

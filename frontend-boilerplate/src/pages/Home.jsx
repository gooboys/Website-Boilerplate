import React from 'react';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <h1 className="text-2xl font-bold text-center">
      <Link to="/about" className="text-blue-600 hover:underline">
        Home Page (click me to go to About)
      </Link>
    </h1>
  );
}
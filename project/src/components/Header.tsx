import React, { useState } from 'react';
import { Beaker, User, Briefcase, Mail, X, Menu } from 'lucide-react';

interface HeaderProps {
  activeSection: string;
}

const Header: React.FC<HeaderProps> = ({ activeSection }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const navItems = [
    { id: 'home', label: 'LAB', icon: Beaker },
    { id: 'about', label: 'FORMULA', icon: User },
    { id: 'projects', label: 'OPERATIONS', icon: Briefcase },
    { id: 'contact', label: 'CONTACT', icon: Mail },
  ];

  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
    setIsMenuOpen(false);
  };

  return (
    <header className="bg-bb-dark/95 backdrop-blur-sm border-b border-bb-green/30 sticky top-0 z-40">
      <div className="max-w-7xl mx-auto px-2 sm:px-4 lg:px-8">
        <div className="flex flex-col md:flex-row justify-between items-center py-3 md:py-4 gap-2 md:gap-0">
          <div className="flex items-center space-x-3">
            <Beaker className="h-10 w-10 text-bb-green animate-glow" />
            <div>
              <span className="text-2xl font-bold bg-gradient-to-r from-bb-green via-bb-yellow to-bb-orange bg-clip-text text-transparent font-oswald tracking-wider">
                HEISENBERG
              </span>
              <div className="text-xs text-bb-green font-mono">99.1% PURE</div>
            </div>
          </div>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex space-x-2">
            {navItems.map((item) => {
              const Icon = item.icon;
              return (
                <button
                  key={item.id}
                  onClick={() => scrollToSection(item.id)}
                  className={`flex items-center space-x-2 px-3 md:px-4 py-2 rounded-lg transition-all duration-300 font-oswald font-semibold focus:outline-none focus:ring-2 focus:ring-bb-yellow focus:ring-offset-2 focus:ring-offset-bb-dark text-base md:text-lg ${
                    activeSection === item.id
                      ? 'bg-bb-green text-bb-dark shadow-lg animate-glow'
                      : 'text-bb-green hover:text-bb-yellow hover:bg-bb-gray/50 border border-bb-green/20 hover:border-bb-yellow/50'
                  }`}
                >
                  <Icon className="h-4 w-4" />
                  <span>{item.label}</span>
                </button>
              );
            })}
          </nav>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden p-3 rounded-lg text-bb-green hover:text-bb-yellow hover:bg-bb-gray/50 transition-colors border border-bb-green/30 focus:outline-none focus:ring-2 focus:ring-bb-yellow focus:ring-offset-2 focus:ring-offset-bb-dark"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            aria-label="Toggle navigation menu"
          >
            {isMenuOpen ? <X className="h-7 w-7" /> : <Menu className="h-7 w-7" />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <nav className="md:hidden bg-bb-dark/95 border-t border-bb-green/30 rounded-b-xl shadow-lg animate-fade-in">
            <ul className="flex flex-col py-4 space-y-2">
              {navItems.map((item) => {
                const Icon = item.icon;
                return (
                  <li key={item.id}>
                    <button
                      onClick={() => scrollToSection(item.id)}
                      className={`w-full flex items-center space-x-3 px-6 py-4 text-lg font-oswald font-semibold rounded-lg transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-bb-yellow focus:ring-offset-2 focus:ring-offset-bb-dark ${
                        activeSection === item.id
                          ? 'bg-bb-green text-bb-dark shadow-lg animate-glow'
                          : 'text-bb-green hover:text-bb-yellow hover:bg-bb-gray/50 border border-bb-green/20 hover:border-bb-yellow/50'
                      }`}
                    >
                      <Icon className="h-5 w-5" />
                      <span>{item.label}</span>
                    </button>
                  </li>
                );
              })}
            </ul>
          </nav>
        )}
      </div>
    </header>
  );
};

export default Header;
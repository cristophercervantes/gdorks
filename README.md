# CyberDork - Advanced Google Dorking Tool

![CyberDork v2.0](https://img.shields.io/badge/CyberDork-v2.0-blue)
![License MIT](https://img.shields.io/badge/License-MIT-green)
![Platform Web](https://img.shields.io/badge/Platform-Web-lightgrey)
![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)

A powerful, web-based Google Dorking tool designed for security researchers and bug bounty hunters to efficiently discover sensitive information and potential vulnerabilities.

**Live Web Version:** https://cristophercervantes.github.io/gdorks/

---

## 🚀 Features

- **Advanced Dork Generation**  
  50+ Pre-configured Dork Categories covering various security testing scenarios.

- **Smart Query Generation** with automatic domain substitution.

- **Multiple Search Engine Support** (Google, Bing, DuckDuckGo).

- **One-Click Search** for instant results.

- **Bulk Copy & Search operations**.

---

## 🎯 Comprehensive Dork Categories

- File Extensions & Parameters (PHP, ASPX, JSP, etc.)
- Authentication & Authorization (Login pages, admin panels)
- Sensitive Files & Directories (Config files, backups, Git exposures)
- Technology-Specific Dorks (WordPress, Joomla, Jenkins, Docker)
- Cloud & Services (AWS S3, cloud storage)
- Error & Debug Information (PHP errors, database errors, stack traces)
- Vulnerability Testing (XSS, SQLi, SSRF, RCE parameters)

---

## 💻 User-Friendly Interface

- Modern Dark Theme optimized for extended usage sessions
- Fully Responsive Design (desktop & mobile)
- Intuitive Category System with expandable sections
- Bulk Operations (Select All, Clear All, Generate All)
- Copy to Clipboard functionality with visual feedback
- Real-time Results Counter
- Professional UI/UX with smooth animations

---

## 🛠️ Installation & Deployment

### 🌐 Live Web Version (Recommended)
Access the tool directly at: https://cristophercervantes.github.io/gdorks/  
No installation required — ready to use immediately.

### Option 1: GitHub Pages Deployment
1. Fork this repository  
2. Enable GitHub Pages in your repository settings (Settings → Pages)  
3. Select source branch (usually `main` or `gh-pages`)  
4. Access your tool at: `https://yourusername.github.io/repository-name`

### Option 2: Local Deployment
```bash
git clone https://github.com/cristophercervantes/gdorks.git
cd gdorks
```

Serve the files using any web server:

```bash
# Using Python 3
python -m http.server 8000

# Using Node.js
npx http-server

# Using PHP
php -S localhost:8000
```

Open http://localhost:8000 in your browser.

### Option 3: Direct File Access
Download `index.html` and open it in any modern web browser.

---

## 📖 Usage Guide

### 🎯 Basic Workflow
1. **Enter Target Domain:** Input the company domain you want to test (e.g., `example.com`)  
2. **Select Dork Categories:** Choose from 50+ pre-configured dork categories  
3. **Generate Dorks:** Click **Generate Dorks** to create customized search queries  
4. **Execute Searches:** Use **Copy** or **Search** buttons to execute dorks in your preferred search engine

### 🔧 Advanced Features
- Bulk Operations: Select multiple dorks across categories  
- Search Engine Toggle: Switch between Google, Bing, and DuckDuckGo  
- One-Click Copy: Copy individual dorks or multiple selections  
- Direct Search: Open search results in new tabs

---

## 🔍 Search Engine Selection

- **Google:** Comprehensive results, good for general reconnaissance  
- **Bing:** Alternative results, sometimes reveals different information  
- **DuckDuckGo:** Privacy-focused, no personalized results

---

## 🏗️ Technical Architecture

**Frontend Stack**
- HTML5: Semantic structure with accessibility features  
- CSS3: Modern styling with CSS Grid, Flexbox, and CSS Variables  
- JavaScript (ES6+): Dynamic functionality with modern JavaScript features  
- Font Awesome 6: Professional iconography throughout the interface

**Key Components**
- Dork Database: Organized collection of 50+ security dorks  
- Category Management: Expandable UI with smooth animations  
- Query Engine: Dynamic dork generation with domain substitution  
- Search Integration: Multi-engine search capability  
- Clipboard API: Modern copy-to-clipboard functionality

---

## ⚙️ Performance Features

- Client-Side Processing: No server dependencies  
- Optimized Rendering: Efficient DOM manipulation  
- Responsive Design: Mobile-first approach  
- Fast Loading: Single HTML file with inline resources

---

## 🔧 Customization

### Adding New Dorks
Edit the `dorks` array in the JavaScript section, for example:

```javascript
{
    category: "Your Category Name",
    items: [
        { 
            name: "Your Dork Name", 
            query: "site:example.com your:dork:query" 
        }
    ]
}
```

### Theme Customization
The CSS uses CSS variables for easy theming. Modify these in the `:root` selector:

```css
:root {
    --primary: #0f172a;
    --secondary: #1e293b;
    --accent: #3b82f6;
    --accent-hover: #2563eb;
    --text: #f8fafc;
    --text-secondary: #cbd5e1;
    --border: #334155;
    --card-bg: #1e293b;
    /* ... more variables */
}
```

---

## ⚠️ Legal & Ethical Usage

### 🛡️ Important Disclaimer
**CyberDork is designed exclusively for authorized security testing and educational purposes.**

**✅ Permitted Use Cases**
- Bug bounty programs with proper authorization  
- Penetration testing with explicit client consent  
- Security research on systems you own or manage  
- Educational purposes and security training  
- Internal security assessments

**❌ Prohibited Use Cases**
- Unauthorized testing of systems you don't own  
- Malicious hacking or cyber attacks  
- Privacy violations or data theft  
- Any illegal activities  
- Testing without explicit permission

### 🔒 Responsible Usage Guidelines
- Always get permission before testing any system  
- Respect `robots.txt` and terms of service  
- Follow responsible disclosure practices  
- Comply with local laws and regulations  
- Use appropriate rate limiting to avoid service disruption

---

## 🐛 Troubleshooting

**Common Issues & Solutions**

- **Dorks not generating?**  
  - Ensure you've entered a target domain in the input field  
  - Verify at least one dork category is selected  
  - Check browser console for JavaScript errors

- **Search not working?**  
  - Check if pop-ups are blocked in your browser  
  - Verify internet connectivity  
  - Try a different search engine option

- **UI looks broken?**  
  - Clear browser cache and hard refresh (Ctrl+F5)  
  - Ensure JavaScript is enabled in your browser  
  - Try using a modern browser (Chrome, Firefox, Safari, Edge)

- **Copy functionality not working?**  
  - Ensure you're accessing via HTTPS (required for Clipboard API)  
  - Try the fallback method (automatic on HTTP)  
  - Check browser permissions for clipboard access

---

## ✅ Browser Compatibility

- Chrome 90+ (Recommended)  
- Firefox 88+  
- Safari 14+  
- Edge 90+  
- Mobile browsers (iOS Safari, Chrome Mobile)

---

## 🤝 Contributing

We welcome contributions from the security community! Here's how you can help:

**Ways to Contribute**
- Report Bugs: Open an issue with detailed description and steps to reproduce  
- Suggest Features: Share your ideas for new features or improvements  
- Submit Dorks: Contribute new, effective dork queries  
- Code Improvements: Submit pull requests for enhancements  
- Documentation: Help improve documentation and usage guides

**Contribution Guidelines**
- Follow existing code style and patterns  
- Test changes thoroughly across different browsers  
- Update documentation as needed  
- Ensure all contributions are legal and ethical  
- Submit pull requests with clear descriptions

**Development Setup**
```bash
# Fork the repository
# Create a feature branch
git checkout -b feature/amazing-feature
git commit -m 'Add amazing feature'
git push origin feature/amazing-feature
# Open a Pull Request
```

---

## 📊 Best Practices & Tips

**For Optimal Usage**
- Start Specific: Begin with targeted dorks rather than broad searches  
- Combine Categories: Use multiple dork categories for comprehensive reconnaissance  
- Verify Results: Always manually verify findings to avoid false positives  
- Document Everything: Keep detailed notes of your testing process and findings

**Performance Tips**
- Use specific domain names for better results  
- Regularly update dork queries as search engines evolve  
- Use different search engines for varied result sets  
- Implement appropriate delays between automated searches

---

## 🛡️ Security Considerations

**For Users**
- Use VPNs or dedicated research infrastructure when appropriate  
- Be aware that search engines may log your queries  
- Consider using dedicated research accounts  
- Follow organizational security policies

**Application Security**
- No sensitive data is stored or transmitted  
- All processing happens client-side in your browser  
- No tracking, analytics, or external dependencies  
- Open source code for transparency and auditability

---

## 📄 License

This project is licensed under the **MIT License** — see the `LICENSE` file for details.

---

## 🙏 Acknowledgments

- Security Research Community — For continuous inspiration and knowledge sharing  
- Open Source Contributors — Everyone who helps improve security tools  
- Bug Bounty Hunters — For developing and sharing effective techniques  
- Browser Developers — For modern web APIs that make tools like this possible

---

## 📞 Support & Community

- **Live Demo:** https://cristophercervantes.github.io/gdorks/  
- **Documentation:** GitHub Wiki  
- **Issues:** GitHub Issues  
- **Discussions:** GitHub Discussions

---

## 🔄 Version History

- **v2.0 (Current):** Enhanced UI, mobile optimization, bulk operations  
- **v1.0:** Initial release with core dorking functionality

---

⚠️ **Legal Notice:** This tool is provided for educational and authorized security testing purposes only. Users are solely responsible for ensuring they have proper authorization before conducting any security testing activities.

**Remember:** With great power comes great responsibility. Always use CyberDork ethically, legally, and with proper authorization.

Happy (and responsible) hunting! 🔍


  document.addEventListener('DOMContentLoaded', function() {
    const subjectColors = {
      maths: '#154360',      // Darker Blue
      chemistry:'#1A5D3C',  // Darker Green
      physics: '#a39a30',    // Lighter Yellow
      english: '#512E5F',    // Darker Purple
      // Add more if needed
    };

    document.querySelectorAll('.subject').forEach(el => {
      const subject = el.dataset.subject.trim();
      const color = subjectColors[subject];

      if (color) {
        el.style.color = color;
      } else {
        el.style.color = 'purple'; // Default fallback
      }
    });
  });


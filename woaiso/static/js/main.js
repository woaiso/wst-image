$(function() {
    $('#bgcolor,#color').colorpicker();
    preview_image = $('#preview-image');
    $('#preview-btn').click(function() {
      params = $('#image-form').serialize();
      preview_image.attr('src', '/x?' + params);
    });
    $('#download-btn').click(function() {
      params = $('#image-form').serialize();
      url = '/x?' + params + '&download=1';
      const ifr = document.createElement('iframe');
      ifr.setAttribute('src', url);
      ifr.setAttribute('style', 'display:none');
      document.body.appendChild(ifr);
      setTimeout(() => document.body.removeChild(ifr), 1000);
    });
  });
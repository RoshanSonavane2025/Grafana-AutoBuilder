// Global variables
let uploadHistory = JSON.parse(localStorage.getItem('uploadHistory') || '[]');
let stats = JSON.parse(localStorage.getItem('dashboardStats') || '{"uploads": 0, "exports": 0, "dashboards": 0}');

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
    updateStats();
    updateHistoryDisplay();
    updateRecentActivity();
    setupFileUpload();
    setupUploadForm();
});


// Navigation
function showPage(pageId) {
    document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
    event.target.classList.add('active');

    document.querySelectorAll('.page-section').forEach(section => section.classList.remove('active'));
    document.getElementById(pageId).classList.add('active');
    // if (pageId === 'history') {
    //     getHistory();
    // }
    if (pageId === 'settings') {
        getCurrentSettings();
    }
    if (pageId === 'upload') {
        getGrafanaFolders();
    }

    const titles = {
        'home': 'Dashboard Overview',
        'upload': 'Upload & Generate Dashboard',
        'history': 'Dashboard History',
        'export': 'Export Dashboard',
        'settings': 'Grafana Settings'
    };
    document.getElementById('pageTitle').textContent = titles[pageId];

    if (window.innerWidth <= 768) {
        document.getElementById('sidebar').classList.remove('open');
    }
}

// Sidebar toggle (mobile)
function toggleSidebar() {
    document.getElementById('sidebar').classList.toggle('open');
}

// File upload setup
function setupFileUpload() {
    const fileUploadArea = document.getElementById('fileUploadArea');
    const csvFile = document.getElementById('csvFile');

    fileUploadArea.addEventListener('click', () => csvFile.click());

    csvFile.addEventListener('change', function() {
        if (this.files.length > 0) {
            const file = this.files[0];
            showFileInfo(file);
        }
    });

    fileUploadArea.addEventListener('dragover', e => { e.preventDefault(); fileUploadArea.classList.add('dragover'); });
    fileUploadArea.addEventListener('dragleave', e => { e.preventDefault(); fileUploadArea.classList.remove('dragover'); });

    fileUploadArea.addEventListener('drop', e => {
        e.preventDefault();
        fileUploadArea.classList.remove('dragover');
        const files = e.dataTransfer.files;
        if (files.length > 0 && files[0].type === 'text/csv') {
            csvFile.files = files;
            showFileInfo(files[0]);
        } else {
            showNotification('Please drop a valid CSV file', 'error');
        }
    });
}

function showFileInfo(file) {
    const fileInfo = document.getElementById('fileInfo');
    fileInfo.innerHTML = `
        <i class="fas fa-file-csv"></i>
        <strong>${file.name}</strong> (${(file.size / 1024).toFixed(1)} KB)
    `;
    fileInfo.style.display = 'block';
}

// Upload form setup
function setupUploadForm() {
    document.getElementById('uploadForm').addEventListener('submit', function(e) {
        e.preventDefault();
        handleUpload();
    });
}

async function handleUpload(event) {
    event.preventDefault(); // prevent form submission reload

    const fileInput = document.getElementById('csvFile');
    const file = fileInput.files[0];
    const folderUID = document.getElementById('folderSelect').value.trim();
    const dashboardName = document.getElementById('dashboardName').value.trim();
    const uploadBtn = document.getElementById('uploadBtn');

    if (!file) {
        showNotification('Please select or drop a CSV file', 'error');
        return;
    }

    // Show uploading state
    uploadBtn.disabled = true;
    uploadBtn.innerHTML = '<div class="loading"></div> Generating Dashboard...';

    try {
        const formData = new FormData();
        formData.append('file', file); // CSV file
        formData.append('folder_uid', folderUID);
        formData.append('dashboardName', dashboardName);

        const response = await fetch('/api/dashboard/generate', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.error || 'Failed to generate dashboard');
        }

        const data = await response.json();

        // Update file info UI
        document.getElementById('fileInfo').style.display = 'none';
        fileInput.value = ''; // reset file input

        addToHistory(file.name, folderUID);
        stats.uploads++;
        stats.dashboards++;
        updateStats();

        showNotification(`Dashboard created: ${data.dashboard_uid}`, 'success');
    } catch (error) {
        showNotification(`Error: ${error.message}`, 'error');
    } finally {
        uploadBtn.disabled = false;
        uploadBtn.innerHTML = '<i class="fas fa-upload"></i> Generate Dashboard';
    }
}

// ---------------- Drag & Drop support ----------------
const fileUploadArea = document.getElementById('fileUploadArea');
const fileInput = document.getElementById('csvFile');
const fileInfo = document.getElementById('fileInfo');

fileUploadArea.addEventListener('click', () => fileInput.click());
fileInput.addEventListener('change', () => displayFileInfo(fileInput.files[0]));

fileUploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    fileUploadArea.classList.add('dragover');
});

fileUploadArea.addEventListener('dragleave', () => {
    fileUploadArea.classList.remove('dragover');
});

fileUploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    fileUploadArea.classList.remove('dragover');
    const droppedFile = e.dataTransfer.files[0];
    fileInput.files = e.dataTransfer.files; // assign to hidden input
    displayFileInfo(droppedFile);
});

function displayFileInfo(file) {
    if (!file) return;
    fileInfo.style.display = 'block';
    fileInfo.textContent = `Selected file: ${file.name} (${(file.size / 1024).toFixed(2)} KB)`;
}

// ---------------- Bind form submit ----------------
document.getElementById('uploadForm').addEventListener('submit', handleUpload);


// Export functionality
async function exportDashboard(format) {
    const dashboardUID = document.getElementById('dashboardUID').value.trim();

    if (!dashboardUID) {
        showNotification('Please enter a dashboard UID', 'error');
        return;
    }

    try {
        showNotification('Preparing export...', 'info');

        const response = await fetch(`/api/dashboard/export?uid=${dashboardUID}&format=${format}`);
        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.error || 'Export failed');
        }

        const blob = await response.blob();
        downloadFile(blob, `dashboard_${dashboardUID}.${format}`, format);

        stats.exports++;
        updateStats();

        showNotification(`Dashboard exported as ${format.toUpperCase()}`, 'success');
    } catch (error) {
        showNotification(`Export failed: ${error.message}`, 'error');
    }
}

function downloadFile(data, filename, format) {
    const url = window.URL.createObjectURL(data);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
    a.remove();
}

// History management
function addToHistory(fileName, folderUID) {
    const historyItem = {
        id: Date.now(),
        fileName,
        folderUID: folderUID || 'Default',
        date: new Date().toLocaleDateString(),
        time: new Date().toLocaleTimeString()
    };

    uploadHistory.unshift(historyItem);
    localStorage.setItem('uploadHistory', JSON.stringify(uploadHistory));
    updateHistoryDisplay();
    updateRecentActivity();
}

// History & stats updates remain unchanged
function updateHistoryDisplay() { 
    const historyList = document.getElementById('historyTable');
    console.log(uploadHistory);
    historyList.innerHTML = '';
    uploadHistory.forEach(item => {
        const listItem = document.createElement('tr');
        listItem.innerHTML = `
            <td>${item.fileName}</td>
            <td>${item.folderUID}</td>
            <td>${item.date} ${item.time}</td>
        `;
        historyList.appendChild(listItem);
    });
 }
function updateRecentActivity() { 
    const recentActivityList = document.getElementById('recentActivity');
    recentActivityList.innerHTML = '';

    uploadHistory.forEach(item => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <span>${item.fileName}</span>
            <span>${item.folderUID}</span>
            <span>${item.date} ${item.time}</span>
        `;
        recentActivityList.appendChild(listItem);
    });
 }
function updateStats() { 
    document.getElementById('totalUploads').textContent = stats.uploads;
    document.getElementById('totalExports').textContent = stats.exports;
    document.getElementById('totalDashboards').textContent = stats.dashboards;
    localStorage.setItem('dashboardStats', JSON.stringify(stats));
 }

// Notifications remain unchanged
function showNotification(message, type = 'info') { 

    const notification = document.createElement('div');
    notification.classList.add('notification', type);
    notification.innerHTML = `
        <i class="fas fa-${getNotificationIcon(type)}"></i>
        ${message}
    `;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.remove();
    }, 5000);

}
function getNotificationIcon(type) { 
    switch (type) {
        case 'success':
            return 'check-circle';
        case 'error':
            return 'exclamation-triangle';
        case 'info':
        default:
            return 'info-circle';
    }
}



function updateSettings(event) {
    event.preventDefault(); // prevent form reload

    const grafanaURL = document.getElementById('grafanaURL').value;
    const grafanaKEY = document.getElementById('grafanaKEY').value;

    fetch('/api/settings', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            grafanaURL: grafanaURL,
            grafanaKEY: grafanaKEY
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            showNotification(data.message, 'success');
        } else {
            showNotification(data.error || 'Failed to update settings', 'error');
        }
    })
    .catch(error => {
        showNotification(`Error: ${error.message}`, 'error');
    });
}

document.getElementById('settingsForm').addEventListener('submit', updateSettings);


function getCurrentSettings() {
    fetch('/api/current_settings')
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch current settings');
            return response.json();
        })
        .then(data => {
            if (data.grafanaURL) {
                document.getElementById('grafanaURL').value = data.grafanaURL;
            }

            if (data.grafanaKEY) {
                // Show read-only display
                document.getElementById('grafanaKeyDisplay').style.display = 'inline';
                document.getElementById('changeKeyBtn').style.display = 'inline-block';
                document.getElementById('grafanaKEY').style.display = 'none';
            } else {
                // If no key configured, show input box
                document.getElementById('grafanaKeyDisplay').style.display = 'none';
                document.getElementById('changeKeyBtn').style.display = 'none';
                document.getElementById('grafanaKEY').style.display = 'block';
            }
        })
        .catch(error => {
            showNotification(`Error loading settings: ${error.message}`, 'error');
            console.error(error);
        });
}

// Show input box when user wants to change key
document.getElementById('changeKeyBtn').addEventListener('click', () => {
    document.getElementById('grafanaKeyDisplay').style.display = 'none';
    document.getElementById('changeKeyBtn').style.display = 'none';
    const keyInput = document.getElementById('grafanaKEY');
    keyInput.style.display = 'block';
    keyInput.value = '';
    keyInput.focus();
});

// Form submit
document.getElementById('settingsForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const url = document.getElementById('grafanaURL').value.trim();
    const keyInput = document.getElementById('grafanaKEY');
    const key = keyInput.style.display === 'block' ? keyInput.value.trim() : null;

    const payload = { grafanaURL: url };
    if (key) payload.grafanaKEY = key;

    try {
        const response = await fetch('/api/settings', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || 'Failed to save settings');

        showNotification('Settings updated successfully', 'success');
        // Reset display if API key was updated
        if (key) {
            document.getElementById('grafanaKeyDisplay').textContent = 'Already Configured';
            document.getElementById('grafanaKeyDisplay').style.display = 'inline';
            document.getElementById('changeKeyBtn').style.display = 'inline-block';
            keyInput.style.display = 'none';
        }
    } catch (err) {
        showNotification(`Error: ${err.message}`, 'error');
    }
});


function getGrafanaFolders() { 
    fetch('/api/grafana/folders')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch Grafana folders');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            grafanaFolders = data || [];  // <- changed this line
            const folderSelect = document.getElementById('folderSelect');
            folderSelect.innerHTML = ''; // clear existing options

            grafanaFolders.forEach(folder => {
                const option = document.createElement('option');
                option.value = folder.uid;
                option.textContent = folder.title;
                folderSelect.appendChild(option);
            });
        })
        .catch(error => {
            showNotification(`Error loading Grafana folders: ${error.message}`, 'error');
            console.error(error);
        });
}


function getHistory() { 
    fetch('/api/dashboard/history')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch history');
            }
            return response.json();
        })
        .then(data => {
            uploadHistory = data.history || [];
            console.log(uploadHistory);
            updateHistoryDisplay();
        })
        .catch(error => {
            showNotification(`Error loading history: ${error.message}`, 'error');
            console.error(error);
        });
}
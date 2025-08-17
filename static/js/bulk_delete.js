document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('bulk-delete-form');
  if (!form) return;

  const deleteBtn = document.getElementById('delete-selected');
  const selectAllBtn = document.getElementById('select-all-btn');
  const countEl = deleteBtn ? deleteBtn.querySelector('.count') : null;

  const allCbs = () => form.querySelectorAll('input[name="ids"]');
  const selCbs = () => form.querySelectorAll('input[name="ids"]:checked');

  function selectedCount() { return selCbs().length; }
  function isAllSelected() {
    const all = allCbs();
    return all.length > 0 && selectedCount() === all.length;
  }
  function setAll(checked) {
    allCbs().forEach(cb => { cb.checked = checked; });
    updateState();
  }

  function updateState() {
    const cnt = selectedCount();
    if (deleteBtn) deleteBtn.disabled = cnt === 0;
    if (countEl) countEl.textContent = cnt;
    if (selectAllBtn) selectAllBtn.textContent = isAllSelected() ? 'Clear' : 'Select all';
  }

  form.addEventListener('change', function (e) {
    if (e.target.matches('input[name="ids"]')) updateState();
  });

  if (selectAllBtn) {
    selectAllBtn.addEventListener('click', function () {
      setAll(!isAllSelected());
    });
  }

  form.addEventListener('submit', function (e) {
    const cnt = selectedCount();
    if (cnt === 0) {
      e.preventDefault();
      alert('Select at least one tattoo to delete.');
      return;
    }
    if (!confirm(`Delete ${cnt} tattoo(s)?`)) {
      e.preventDefault();
    }
  });

  updateState();
});
